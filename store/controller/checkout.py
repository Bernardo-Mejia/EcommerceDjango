from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from store.models import Cart, Order, OrderItem, Product, Profile

import random


@login_required(login_url="loginpage")
def index(request):
    rawCart = Cart.objects.filter(user=request.user)
    for item in rawCart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)

    cartItems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartItems:
        total_price += total_price + item.product.selling_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()

    context = {
        "cartItems": cartItems,
        "total_price": total_price,
        "userprofile": userprofile,
    }
    return render(request, "store/checkout.html", context)


@login_required(login_url="loginpage")
def placeorder(request):
    if request.method == "POST":
        currentUser = User.objects.filter(id=request.user.id).first()

        if not currentUser.first_name:
            currentUser.first_name = request.POST.get("fname")
            currentUser.last_name = request.POST.get("lname")
            # currentUser.email = request.POST.get("email")
            currentUser.save()

        if not Profile.objects.filter(user=request.user):
            userProfile = Profile()
            userProfile.user = request.user
            userProfile.phone = request.POST.get("phone")
            userProfile.address = request.POST.get("address")
            userProfile.city = request.POST.get("city")
            userProfile.state = request.POST.get("state")
            userProfile.country = request.POST.get("country")
            userProfile.pincode = request.POST.get("pincode")
            userProfile.save()

        newOrder = Order()
        newOrder.user = request.user
        newOrder.fname = request.POST.get("fname")
        newOrder.lname = request.POST.get("lname")
        newOrder.email = request.POST.get("email")
        newOrder.phone = request.POST.get("phone")
        newOrder.address = request.POST.get("address")
        newOrder.city = request.POST.get("city")
        newOrder.state = request.POST.get("state")
        newOrder.country = request.POST.get("country")
        newOrder.pincode = request.POST.get("pincode")

        newOrder.payment_mode = request.POST.get("payment_mode")

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty

        newOrder.total_price = cart_total_price

        newOrder.save()

        newOrderItems = Cart.objects.filter(user=request.user)
        for item in newOrderItems:
            OrderItem.objects.create(
                order=newOrder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty,
            )

            # ? To decrese the product quantity from available stock
            orderProduct = Product.objects.filter(id=item.product_id).first()
            orderProduct.quantity = orderProduct.quantity - item.product_qty
            orderProduct.save()

        # ? To clear user's Cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, "Your order has been placed successfully")

    return redirect("/")
