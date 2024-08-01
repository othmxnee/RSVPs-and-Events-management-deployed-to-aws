 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class RSVP(models.Model):
    STATUS_CHOICES = [
        ('attending', 'Attending'),
        ('not_attending', 'Not Attending'),
        ('maybe', 'Maybe'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')  # Ensures a user can RSVP to the same event only once

    def __str__(self):
        return f"{self.user.username} - {self.event.name} - {self.status}"

class Invitation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    rsvp_response = models.BooleanField(null=True, blank=True)  # None for no response, True for attending, False for not attending
    timestamp = models.DateTimeField(auto_now_add=True)

    card_sent = models.BooleanField(default=False)  # Track if the card has been sent

    def __str__(self):
        return f'Invitation from {self.sender.username} to {self.recipient.username} for {self.event.name}'

