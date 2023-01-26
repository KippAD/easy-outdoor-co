from django.shortcuts import render
from django.views import View
from products.models import Product
import random


def index(request):
    """Displays home page"""
    products = list(Product.objects.all())
    random_products = random.sample(products, k=8)
    user = request.user
    context = {
        'related_products': random_products,
        'user': user,
    }

    return render(request, 'home/index.html', context)


def frequently_asked_questions(request):
    """Displays faq page"""
    return render(request, 'home/faq.html')