from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_welcome_email(self, user_id):
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
        send_mail(
            subject='Welcome to Job Portal',
            message=f'Hello {user.username}, welcome to Job Portal!',
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False,
        )
        logger.info(f"Welcome email sent to user {user.username} ({user.email})")
        return f"Email sent to {user.email}"
    except Exception as e:
        logger.error(f"Failed to send welcome email to user_id {user_id}: {e}")
        return f"Failed to send email: {e}" 