# events/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Invitation
from django.core.mail import send_mail
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Invitation)
def send_card(sender, instance, created, **kwargs):
    logger.info(f"Signal triggered for Invitation ID {instance.id}")
    
    # Log the current state of the invitation
    logger.info(f"Before condition check - RSVP Response: {instance.rsvp_response}, Card Sent: {instance.card_sent} (type: {type(instance.card_sent)})")
    
    # Check conditions
    if instance.rsvp_response and not instance.card_sent:
        logger.info("RSVP response is True and card_sent is False. Preparing to send email...")

        # Compose the email content
        card_content = (
            f"Event: {instance.event.title}\n"
            f"Location: {instance.event.location}\n"
            f"Date: {instance.event.date}\n\n"
            f"Message from {instance.sender.username}: {instance.message}"
        )

        try:
            # Send the email
            send_mail(
                subject='Your Event Card',
                message=card_content,
                from_email='no-reply@example.com',
                recipient_list=[instance.recipient.email],
                fail_silently=False,
            )
            logger.info(f"Email sent successfully to {instance.recipient.email}")

            # Update card_sent to True
            instance.card_sent = True
            instance.save(update_fields=['card_sent'])
            logger.info(f"Updated card_sent to True for Invitation ID {instance.id}")
        
        except Exception as e:
            logger.error(f"Error sending email: {e}")
    else:
        logger.info("No action taken: Either RSVP response is not True or card has already been sent.")
