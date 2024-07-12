from django.urls import path,include
from IniciarSesion.views import *
from registro.views import registroView
from carta.views import carta
from .views import quienesSomosView
from home.views import homeView

urlpatterns=[
    path('home/',homeView, name='homeView'),
    path('login/',loginView,name='login'),
    path('register/',registroView,name='registro'),
    path('menu/',carta,name='carta'),
    path('quienesSomos/',quienesSomosView,name='quienesSomosView'),


]