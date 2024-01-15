from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Cart


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
