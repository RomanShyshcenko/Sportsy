import os

import pytest

from django.urls import reverse
from rest_framework import status

from user.models import Profile, PhoneNumbers
from rest_framework_simplejwt.tokens import AccessToken

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

import configurations

configurations.setup()


def create_user(django_user_model):
    user = django_user_model.objects.create_user(
        email='test@email.com', password='password'
    )
    profile = Profile.objects.create(user=user, first_name='test', last_name='test')
    phone_number = PhoneNumbers.objects.create(user=user)

    return user, profile, phone_number


@pytest.mark.django_db
def test_invalid_token(client):
    url = reverse('user:retrieve')

    headers = {'HTTP_AUTHORIZATION': f'Bearer invalid_token'}
    response = client.get(url, **headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_create_user_fail(client, django_user_model):
    url = reverse('user:create')
    create_user(django_user_model)
    invalid_data = [
        {},  # No data
        {"email": "example@gmail.com", "password": "", "confirm_password": ""},  # No passwords
        {"email": "example_gmail.com", "password": "12345678", "confirm_password": "12345678"},  # Invalid email
        {"email": "test@email.com", "password": "12345678", "confirm_password": "12345678"},  # Email already exists
        {"email": "example@gmail.com", "password": "12345678", "confirm_password": "12345"},  # invalid confirm password
        {"email": "example@gmail.com", "password": "12345678", "confirm_password": "12345678999"},
        # Invalid confirm password
    ]
    for data in invalid_data:
        response = client.post(url, data, format='json')
        assert response.status_code == 400


@pytest.mark.django_db
def test_create_user(client):
    """Test creating a new user"""
    payload = {'email': 'test@gmail.com', 'password': 'password12345', 'confirm_password': 'password12345'}
    url = reverse('user:create')
    response = client.post(url, data=payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_retrieve_user(client, django_user_model):
    user, profile, phone_number = create_user(django_user_model)
    token = AccessToken.for_user(user)
    url = reverse('user:retrieve')
    headers = {'HTTP_AUTHORIZATION': f'Bearer {str(token)}'}

    response = client.get(url, **headers)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_user(client, django_user_model):
    user, profile, phone_number = create_user(django_user_model)
    token = AccessToken.for_user(user)
    data = {
        "email": 'test@email.com',
        "username": 'test@username',
        "profile": {
            "first_name": "first_name",
            "last_name": "example",
            "country": "example",
            "gender": "MA",
        }
    }
    response = client.put(
        reverse('user:update'),
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {str(token)}"
    )
    response_content = response.json()
    print(response_content)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_email_update(client, django_user_model):
    user, profile, phone_number = create_user(django_user_model)
    token = AccessToken.for_user(user)
    data = {
        "email": "example@gmail.com"
    }
    response = client.put(
        reverse('user:change-email'),
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {str(token)}"
    )
    assert response.status_code == 200
    assert django_user_model.objects.filter(email=data['email'], is_confirmed_email=False).exists()


@pytest.mark.django_db
def test_email_verification(client, django_user_model):
    pass


@pytest.mark.django_db
def test_email_verification_fail(client):
    pass


@pytest.mark.django_db
def test_change_password(client, django_user_model):
    user, _, _ = create_user(django_user_model)
    url = reverse('user:change-password')
    data = {
        "old_password": "password",
        "new_password": "password123",
        "confirm_password": "password123"
    }
    token = AccessToken.for_user(user)

    response = client.put(url, data=data, content_type="application/json",
                          HTTP_AUTHORIZATION=f"Bearer {str(token)}")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_login(client, django_user_model):
    user, _, _ = create_user(django_user_model)
    url = reverse('user:token_obtain_pair')

    response = client.post(url, data={'email': user.email, "password": 'password'})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_login_fail(client, django_user_model):
    user, _, _ = create_user(django_user_model)
    url = reverse('user:token_obtain_pair')

    response = client.post(url, data={'email': user.email, "password": 'password123'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
