from django.urls import path

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', view=home, name='home'),
    path('collections', view=collections, name='collections'),
    path('collections/<str:slug>', view=collectionsview, name='collectionsview'),
    path('collection/<str:cat_slug>/<str:prod_slug>', view=productview, name='productview')
]