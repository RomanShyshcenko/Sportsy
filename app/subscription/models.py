from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subscription(models.Model):
    creator_uuid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.FileField(blank=True, null=True)

    price = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        db_table = 'subscriptions'


class UserSubscription(models.Model):
    user_uuid = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_uuid = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    receive_notifications = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user_uuid', 'subscription_uuid')
        ordering = ('-created_at',)
        get_latest_by = 'created_at'
        db_table = 'user_subscriptions'
