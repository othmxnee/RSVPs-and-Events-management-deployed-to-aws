from rest_framework import viewsets, permissions,status
from .serializers import EventModelSerializer,InvitationSerializer
from .models import Event,RSVP,Invitation
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

class SingleEventView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventModelSerializer
    def get_queryset(self):
        return Event.objects.filter(pk = self.kwargs['pk'])
    


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Only return invitations where the recipient is the current user
        return Invitation.objects.filter(recipient=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def update(self, request, *args, **kwargs):
        invitation = self.get_object()
        data = request.data
        if invitation.recipient != request.user :
            raise PermissionDenied("You do not have permission to respond to this invitation.")


        if 'rsvp_response' in data:
            invitation.rsvp_response = data['rsvp_response']
            invitation.save()
            return Response({"status": "RSVP updated"}, status=status.HTTP_200_OK)

        return super().update(request, *args, **kwargs)
    