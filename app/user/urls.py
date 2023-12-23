from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from app.user import views

app_name = 'user'

urlpatterns = [
    path('users', include)
]

user_urlpatterns = [
    path('users/', views.RegisterUserAPIView.as_view(), name='create'),
    path('users/', views.RetrieveUserAPIView.as_view(), name='retrieve'),
    path('users/update/', views.UpdateUserAPIView.as_view(), name='update'),

    path('users/change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    path('users/chage-email/', views.ChangeEmailAPIView.as_view(), name='change-email'),

    path('users/'),  # implement email verification later
    path('users/'),  # implement phone_number verification later

    path('token/', obtain_jwt_token, name='login'),
    path('token/refresh/', refresh_jwt_token, name='refresh'),
    path('token/verify/', verify_jwt_token, name='verify')
]
