from django.urls import path

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .controller import authview, cart, wishlist, checkout

urlpatterns = [
    path('', view=home, name='home'),
    path('collections', view=collections, name='collections'),
    path('collections/<str:slug>', view=collectionsview, name='collectionsview'),
    path('collection/<str:cat_slug>/<str:prod_slug>', view=productview, name='productview'),

    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

    path("wishlist", wishlist.index, name="wishlist"),
    path("add-to-wishlist", wishlist.addtowishlist, name="addtowishlist"),
    path("delete-wishlist-item", wishlist.deletewishlist, name="deletewishlist"),

    path("checkout", checkout.index, name="checkout"),
]