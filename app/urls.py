from django.urls import path 
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path('add/', Add.as_view(), name='add'),
]