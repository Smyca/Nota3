from django.urls import path
from IniciarSesion.views import loginView

urlpatterns=[
    path('login/',loginView, name='login'),
]