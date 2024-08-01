from rest_framework import serializers
from .models import Event, RSVP, Invitation
from django.contrib.auth.models import User

class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    recipient_username = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Invitation
        fields = ['id', 'sender', 'recipient', 'recipient_username', 'event', 'message', 'rsvp_response']
        read_only_fields = ['sender', 'recipient']

    def update(self, instance, validated_data):
        print(f"Updating RSVP response from {instance.rsvp_response} to {validated_data.get('rsvp_response')}")
        instance.rsvp_response = validated_data.get('rsvp_response', instance.rsvp_response)
        instance.save()
        return instance

    def validate(self, data):
        request_user = self.context['request'].user

        # Check if recipient_username is present (only for creation)
        if 'recipient_username' in data:
            # Prevent self-invitation
            if data['recipient_username'] == request_user.username:
                raise serializers.ValidationError("You cannot invite yourself.")

            # Check if the recipient username exists
            try:
                recipient_user = User.objects.get(username=data['recipient_username'])
            except User.DoesNotExist:
                raise serializers.ValidationError("Recipient user does not exist.")

            # Check if the invitation already exists
            if Invitation.objects.filter(recipient=recipient_user, event=data['event']).exists():
                raise serializers.ValidationError("This user has already been invited to this event.")

            data['recipient'] = recipient_user
        
        return data

    def create(self, validated_data):
        validated_data.pop('recipient_username', None)  # Remove recipient_username from validated data
        return super().create(validated_data)
