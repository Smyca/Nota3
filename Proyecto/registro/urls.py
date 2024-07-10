from django.urls import path
from .views import registroView
from home.views import *

urlpatterns=[
    path('registro/',registroView, name='registro'),
    path('',homeView,name='inicio')
]