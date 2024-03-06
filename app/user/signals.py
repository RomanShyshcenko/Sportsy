from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from user.models import PhoneNumber, Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_address(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_phone_number(sender, instance, created, *args, **kwargs):
    if created:
        PhoneNumber.objects.create(user=instance)
