from django.urls import path
from .views import inicio_pagina

urlpatterns = [
    path ('', inicio_pagina, name = 'inicio')
]
