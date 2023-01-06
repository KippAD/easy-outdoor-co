from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A list of all products in the database """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

