from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import sys
from user import views

app_name = 'user'

urlpatterns = [
    path('users/create/', views.RegisterUserAPIView.as_view(), name='create'),
    path('users/', views.RetrieveUserAPIView.as_view(), name='retrieve'),
    path('users/update/', views.UpdateUserAPIView.as_view(), name='update'),

    path('users/change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    path('users/chage-email/', views.ChangeEmailAPIView.as_view(), name='change-email'),

    path('users/email-verification/send/', views.SendEmailVerification.as_view(), name='send-email-verification'),
    path('users/email-verification/verify/', views.EmailVerification.as_view(), name='email-verification'),

    # path('users/'),  # implement phone_number verification later

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
