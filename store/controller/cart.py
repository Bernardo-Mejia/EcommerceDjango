from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from store.forms import CustomUserForm
from store.models import Product, Cart


def addtocart(request):
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                prod_id = int(request.POST.get('product_id'))
                product_check = Product.objects.get(id=prod_id)
                if product_check:
                    if Cart.objects.filter(user=request.user.id, product=prod_id):
                        return JsonResponse({'message': 'Product already in Cart', 'status':'info'})
                    else:
                        prod_qty = int(request.POST.get('product_qty'))
                        if product_check.quantity >= prod_qty:
                            Cart.objects.create(
                                user=request.user, product=product_check, product_qty=prod_qty
                            )
                            return JsonResponse({'message': 'Product added successfully', 'status':'success'})
                        else:
                            return JsonResponse(
                                {
                                    'message': f'Only {str(product_check.quantity)} quantity available',
                                    'status':'warning'
                                }
                            )

                else:
                    return JsonResponse({'message': 'No such propduct found', 'status':'error'})
            else:
                return JsonResponse({'message': 'Login to continue', 'status':'warning'})
        else:
            return redirect('/')
    except Exception as e:
        return JsonResponse({'message': 'Error: ' + str(e), 'status':'error'})


def viewcart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user = request.user)
        context = {"cart": cart}
        return render(request, "store/cart.html", context)
    else:
        messages.error(request, "You must be logged")
        return redirect("/")
    
def updatecart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        if(Cart.objects.filter(user=request.user, product_id = prod_id)):
            prod_qty = int(request.POST.get("product_qty"))
            cart = Cart.objects.get(user=request.user, product_id = prod_id)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'message': 'Updated successfully', 'status':'success'})
    return redirect("/")

def deletecartitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        if(Cart.objects.filter(user=request.user, product_id = prod_id)):
            cartitem = Cart.objects.get(product_id = prod_id, user = request.user)
            cartitem.delete()
            return JsonResponse({'message': 'Deleted successfully', 'status':'success'})
    return redirect("/")