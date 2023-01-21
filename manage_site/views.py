from django.shortcuts import render, reverse
from products.models import Product, SizeStock, RegularStock
from checkout.models import Order
from profiles.models import UserProfile
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from itertools import chain


def manage_site(request):
    """Displays site management template for admin"""
    template = 'manage_site/manage_site.html'

    products = Product.objects.all()
    size_stock = SizeStock.objects.all()
    regular_stock = RegularStock.objects.all()
    orders = Order.objects.all()

    context = {
        'products': products,
        'regular_stock': regular_stock,
        'size_stock': size_stock,
        'orders': orders,
    }

    return render(request, 'manage_site/manage-site.html', context)


class AddProduct(SuccessMessageMixin, generic.CreateView):
    model = Product
    fields = '__all__'
    template_name = "manage_site/add-product.html"
    success_message = "Product Added!"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(AddProduct, self).get_form(form_class)
        form.fields['category'].widget.attrs = {'placeholder': 'Category *'}
        form.fields['name'].widget.attrs = {'placeholder': 'Name *'}
        form.fields['desc'].widget.attrs = {'placeholder': 'Description *'}
        form.fields['slug'].widget.attrs = {'placeholder': 'Slug (Auto-Completes if blank)'}
        form.fields['price'].widget.attrs = {'placeholder': 'Price *'}
        form.fields['sale_price'].widget.attrs = {'placeholder': 'Discounted Price'}
        form.fields['image_url'].widget.attrs = {'placeholder': 'Image URL *'}
        return form

    def get_success_url(self):
        return reverse('manage_site')
