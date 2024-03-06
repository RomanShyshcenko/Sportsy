import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_countries.fields import CountryField

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
    email = models.EmailField(unique=True, db_index=True, max_length=256)
    password = models.CharField(
        max_length=256, blank=True
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

    def activate_email(self):
        self.is_confirmed_email = True

    def deactivate_email(self):
        self.is_confirmed_email = False

    def verify_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)

    def join_as_author(self):
        self.is_author = True

    class Meta:
        db_table = 'users'
        ordering = ('-created_at',)


class PhoneNumber(models.Model):
    user = models.OneToOneField(
        User, related_name='phone',
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17, unique=True,
        null=True, db_index=True
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
        NO_OTHERS = 'JR', _('NO OTHERS)')

    user = models.OneToOneField('User', related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55, blank=True, db_index=True)
    last_name = models.CharField(max_length=55, blank=True, db_index=True)
    country = CountryField(blank_label='(select country)')
    gender = models.CharField(choices=Gender.choices, max_length=2)
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def deactivate(self):
        self.is_active = False

    def get_gender(self) -> Gender:
        # Get value from choices enum
        return self.Gender[str(self.gender)]

    class Meta:
        ordering = ('-created_at',)
        db_table = 'profiles'
