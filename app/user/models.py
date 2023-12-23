import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manegers import CustomUserManager

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_("Phone number must be entered in the "
              "format: '+999999999'. Up to 15 digits allowed.")
)
password_regex = RegexValidator(
    regex=r'^.{8,}$',
    message=_('Password too short')
)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=256,
        validators=[password_regex],
        blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_author = models.BooleanField(default=False)
    is_confirmed_email = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def verify_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)

    class Meta:
        db_table = 'users'
        ordering = ('-created_at',)


class PhoneNumbers(models.Model):
    user = models.OneToOneField(
        User, related_name='phone',
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        null=True
    )
    is_verified = models.BooleanField(default=False)
    sent = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ('-created_at',)
        db_table = 'phone_numbers'


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MA', _('Male')
        FEMALE = 'FE', _('Female')
        NO_OTHERS = 'JR', _('NO OTHERS')

    user = models.OneToOneField('User', related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=True)
    country = models.CharField()  # later replace with django country field
    gender = models.CharField(choices=Gender.choices, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_gender(self) -> Gender:
        # Get value from choices enum
        return self.Gender[str(self.gender)]
