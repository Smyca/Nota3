from django.urls import path
from .views import login_pagina

urlpatterns = [
    path ('login/', login_pagina, name = 'login')
]