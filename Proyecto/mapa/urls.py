from django.urls import include,path
from .views import mapaView

urlpatterns=[

    path('mapa/',mapaView,name='mapa')

]