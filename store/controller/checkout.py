from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Cart, Order, OrderItem, Product

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

    context = {"cartItems": cartItems, "total_price": total_price}
    return render(request, "store/checkout.html", context)


@login_required(login_url="loginpage")
def placeorder(request):
    if request.method == "POST":
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
