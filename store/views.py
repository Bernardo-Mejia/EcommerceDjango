from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *


# Create your views here.
def home(request):
    return render(request, "store/index.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context = {"category": category}
    return render(request, "store/collections.html", context)


def collectionsview(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug, status=0)
        category_name = Category.objects.filter(slug=slug).first()
        context = {"products": products, "category": category_name}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect("collections")


def productview(request, cat_slug, prod_slug):
    if Category.objects.filter(slug=cat_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {"products": products}
        else:
            messages.error(request, "No such product found")
            return redirect("collections")
    else:
        messages.error(request, "No such category found")
        return redirect("collections")
    return render(request, "store/products/view.html", context)


def productListAJAX(request):
    products = Product.objects.filter(status=0).values_list("name", flat=True)
    # Convert JSON products in Array
    productList = list(products)
    return JsonResponse(productList, safe=False)


def searchProduct(request):
    if request.method == "POST":
        searchTerm = request.POST.get("productSearch")
        if searchTerm == "":
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            product = Product.objects.filter(name__contains=searchTerm).first()

            if product:
                return redirect(f"collection/{product.category.slug}/{product.slug}")
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get("HTTP_REFERER"))

    return redirect(request.META.get("HTTP_REFERER"))
