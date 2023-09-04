from django.urls import path

from django.urls import path
from .views import *

urlpatterns = [
    path('', view=home, name='home'),
    path('collections', view=collections, name='collections'),
]