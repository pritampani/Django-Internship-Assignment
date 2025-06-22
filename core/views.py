from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from core.tasks import send_welcome_email
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello from Protected API!", "user": request.user.username})
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password or not email:
            return Response({"error": "username, password, and email are required."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        send_welcome_email.delay(user.id)
        return Response({"message": "User registered successfully.", "token": token.key}, status=status.HTTP_201_CREATED)
@method_decorator(csrf_exempt, name='dispatch')
class TelegramWebhookView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        message = data.get('message')
        if not message:
            return Response({'ok': False, 'error': 'No message found'}, status=400)
        chat = message.get('chat', {})
        telegram_id = str(chat.get('id'))
        username = chat.get('username')
        first_name = chat.get('first_name')
        last_name = chat.get('last_name')
        text = message.get('text', '')
        # Only handle /start command
        if text.strip().startswith('/start'):
            user, created = TelegramUser.objects.update_or_create(
                telegram_id=telegram_id,
                defaults={
                    'telegram_username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                }
            )
            # Send confirmation message
            bot_token = settings.TELEGRAM_BOT_TOKEN_WEBHOOK if hasattr(settings, 'TELEGRAM_BOT_TOKEN_WEBHOOK') else None
            if not bot_token:
                bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN_WEBHOOK', None)
            if not bot_token:
                logger.error('TELEGRAM_BOT_TOKEN_WEBHOOK not set in environment')
                return Response({'ok': False, 'error': 'Bot token not configured'}, status=500)
            send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            payload = {
                'chat_id': telegram_id,
                'text': 'Welcome! Your information has been recorded.'
            }
            try:
                resp = requests.post(send_url, json=payload, timeout=10)
                resp.raise_for_status()
                logger.info(f"Confirmation sent to Telegram user {telegram_id}")
            except Exception as e:
                logger.error(f"Failed to send Telegram message: {e}")
                return Response({'ok': False, 'error': 'Failed to send message'}, status=500)
            return Response({'ok': True, 'message': 'User info recorded and confirmation sent.'})
        return Response({'ok': True, 'message': 'No action taken.'})
