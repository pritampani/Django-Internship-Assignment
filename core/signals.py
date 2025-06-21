""" performing a very important job related to automatic token creation for newly registered users in Django Rest Framework (DRF)
Automatically creates DRF Token when a new User is saved.
Saves you from writing token creation logic in views or serializers.
Enables TokenAuthentication to work out-of-the-box right after user signup.

"""

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance) 