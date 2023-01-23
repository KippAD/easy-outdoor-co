from django.shortcuts import render
from django.views import View
from products.models import Product
import random


# Taken from https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317
def HomePage(request):
    products = list(Product.objects.all())

    random_products = random.choices(products, k=8)

    context = {
        'products': random_products,
    }

    return render(request, 'home/index.html', context)