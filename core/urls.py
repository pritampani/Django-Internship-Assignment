from django.urls import path
from .views import PublicView, ProtectedView, RegisterView, TelegramWebhookView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public-api'),
    path('protected/', ProtectedView.as_view(), name='protected-api'),
    path('register/', RegisterView.as_view(), name='register-api'),
    path('telegram/webhook/', TelegramWebhookView.as_view(), name='telegram-webhook'),
]