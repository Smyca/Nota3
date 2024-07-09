from django.urls import path
from .views import inicio_pagina
from login.views import login_pagina

urlpatterns = [
    path ('', inicio_pagina, name = 'inicio'),
    path('/login',login_pagina, name='login')
]
