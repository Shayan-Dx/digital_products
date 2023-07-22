from django.urls import path

from .views import SubscriptionView, PackageView


urlpatterns = [
    path('subscriptions/', SubscriptionView.as_view()),
    path('packages/', PackageView.as_view()),
]