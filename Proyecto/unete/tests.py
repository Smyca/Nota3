from django.test import TestCase
from home.views import homeView
from .views import uneteView

# Create your tests here.
urlpatterns=[
    path('home/',homeView, name='homeView'),
    path('',uneteView, name='unete'),
    


]