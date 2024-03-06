from django.urls import path

from subscription import views

app_name = 'subscription'

urlpatterns = [
    path('subscriptions/create/', views.SubscriptionCreateAPIView.as_view(), name='create-subscription'),
    path('subscriptions/', views.SubscriptionRetrieveUpdateAPIView.as_view(), name='retrieve-subscription')
]
