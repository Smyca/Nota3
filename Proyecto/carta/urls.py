from django.urls import path
from .views import carta
from home.views import homeView
from IniciarSesion.views import loginView
from registro.views import registroView
from QuienesSomos.views import quienesSomosView

urlpatterns = [
    path ('carta/', carta, name = 'carta'),
    path('home/',homeView, name='homeView'),
    path('login/',loginView,name='login'),
    path('register/',registroView,name='registro'),
    path('quienesSomos/',quienesSomosView,name='quienesSomosView'),

]