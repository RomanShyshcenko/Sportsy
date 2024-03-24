import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.core.files.uploadedfile import SimpleUploadedFile

from user.tests.test_views import create_author
from subscription.models import Subscription, UserSubscription


@pytest.fixture
def image_file():
    # Load your image file here, replace 'example.jpg' with your actual file path
    with open('subscription/tests/test_image.png', 'rb') as f:
        return SimpleUploadedFile('example.jpg', f.read(), content_type='image/jpeg')


@pytest.mark.django_db
def test_subscription_create_view(client, django_user_model, image_file):
    url = reverse('subscription:create-subscription')
    token = AccessToken.for_user(create_author(django_user_model))
    response = client.post(
        url,
        {
            'name': 'example', 'description': 'example',
            'cover_image': image_file, 'price': 12
        },
        HTTP_AUTHORIZATION=f"Bearer {str(token)}",
        format='multipart')

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_subscription_view(client, django_user_model, image_file):
    url = reverse('subscription:retrieve-subscription')
    Subscription.objects.create(
        creator=create_author(django_user_model),
        name='name',
        description='description',
        cover_image=image_file,
        price=12
    )
    response = client.get(url + '?pk=2')
    print(response.status_code)

    assert response.status_code == status.HTTP_200_OK


