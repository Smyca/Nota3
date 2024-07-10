from django.urls import path,include
from .views import homeView
from IniciarSesion.views import *
from registro.views import registroView

urlpatterns=[
    path('',homeView, name='homeView'),
    path('',loginView,name='login'),
    path('',registroView,name='registro'),


]