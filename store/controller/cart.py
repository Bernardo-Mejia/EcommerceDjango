from django.http import JsonResponse
from django.shortcuts import redirect, render
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
