from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user import views

app_name = 'user'

urlpatterns = [
    # registration
    path('users/create/', views.RegisterUserAPIView.as_view(), name='create'),

    path('users/', views.RetrieveUserAPIView.as_view(), name='retrieve'),
    path('users/update/', views.UpdateUserAPIView.as_view(), name='update'),

    path('users/change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    path('users/change-email/', views.ChangeEmailAPIView.as_view(), name='change-email'),

    path('users/email-verification/send/', views.SendEmailVerification.as_view(),
         name='send-email-verification'),
    path('users/email-verification/verify/', views.EmailVerification.as_view(),
         name='email-verification'),
    path('users/forget-password/send/', views.SendResetPasswordEmailAPIView.as_view(),
         name='send_reset_password_email'),
    path('users/forget-password/reset/', views.ResetPasswordAPIView.as_view(),
         name='reset_password'),
    # path('users/'),  # implement phone_number verification later
    path('users/logout/', views.logout_user_view, name='logout'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
