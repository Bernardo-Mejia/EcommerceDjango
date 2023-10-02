from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from store.forms import CustomUserForm
from store.models import Product, Cart, WishList


@login_required(login_url="loginpage")
def index(request):
    wishListItems = WishList.objects.filter(user=request.user)
    context = {"wishlist": wishListItems}
    return render(request, "store/wishlist.html", context)


def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if WishList.objects.filter(user=request.user.id, product=prod_id):
                    return JsonResponse(
                        {"message": "Product already in Wish List", "status": "info"}
                    )
                else:
                    WishList.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse(
                        {"message": "Product added to Wish List", "status": "success"}
                    )
            else:
                return JsonResponse(
                    {"message": "No such propduct found", "status": "error"}
                )
        else:
            return JsonResponse({"message": "Login to continue", "status": "warning"})
    return redirect("/")


def deletewishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            if WishList.objects.filter(user=request.user.id, product=prod_id):
                wishlistitems = WishList.objects.filter(
                    user=request.user, product_id=prod_id
                )
                wishlistitems.delete()
                return JsonResponse(
                    {"message": "Product removed from Wish List", "status": "success"}
                )
            else:
                return JsonResponse(
                    {"message": "Product not found in Wish List", "status": "error"}
                )
        else:
            return JsonResponse({"message": "Login to continue", "status": "warning"})
    return redirect("/")
