from django.urls import path
from .views import PublicView, ProtectedView, RegisterView, TelegramWebhookView

urlpatterns = [
    path('api/v1/public/', PublicView.as_view(), name='public-api'),
    path('api/v1/protected/', ProtectedView.as_view(), name='protected-api'),
    path('api/v1/register/', RegisterView.as_view(), name='register-api'),
    path('api/v1/telegram/webhook/', TelegramWebhookView.as_view(), name='telegram-webhook'),
] 