from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=64, unique=True, db_index=True)
    telegram_username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telegram_username or self.telegram_id