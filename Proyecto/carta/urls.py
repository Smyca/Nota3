from django.urls import path
from .views import carta

urlpatterns = [
    path ('carta/', carta, name = 'carta'),
]