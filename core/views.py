from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from core.task import send_welcome_email
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import TelegramUser
import requests
import logging

logger = logging.getLogger(__name__)
class PublicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Hello from Public API!"})


class ProtectedView(APIView):

    pass
class RegisterView(APIView):

    pass

class TelegramWebhookView(APIView):

    pass
