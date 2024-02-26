from django.db import models
from django.contrib.auth import get_user_model
from core.settings.storage_backend import PublicMediaStorage

User = get_user_model()


class Subscription(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=455)
    cover_image = models.FileField(storage=PublicMediaStorage(), blank=True, null=True)
    price = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        db_table = 'subscriptions'


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    receive_notifications = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'subscription')
        ordering = ('-created_at',)
        get_latest_by = 'created_at'
        db_table = 'user_subscriptions'
