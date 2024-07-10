from django.urls import path,include
from .views import homeView

urlpatterns=[
    path('',homeView, name='homeView')

]