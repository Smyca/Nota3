from django.urls import path,include
from home.views import homeView
from .views import uneteView

# Create your tests here.
urlpatterns=[
    path('home/',homeView, name='homeView'),
    path('unete/',uneteView, name='unete'),
    


]