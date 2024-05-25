from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserProfileView, upgrade_to_author

urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('upgrade/', upgrade_to_author),
]