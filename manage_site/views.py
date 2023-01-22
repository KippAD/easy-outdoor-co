from django.shortcuts import render, reverse
from products.models import Product, SizeStock, RegularStock
from checkout.models import Order
from profiles.models import UserProfile
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from itertools import chain
from .forms import ProductForm


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


# CRUD for products for admin area
class AddProduct(SuccessMessageMixin, generic.CreateView):
    """Creates product model"""
    model = Product
    form_class = ProductForm
    template_name = "manage_site/product-add.html"
    success_message = "Product Added!"

    def get_success_url(self):
        return reverse('manage_site')


class UpdateProduct(SuccessMessageMixin, generic.UpdateView):
    """Updates product model"""
    model = Product
    template_name = "manage_site/product-update.html"
    fields = '__all__'
    success_message = "Product Updated!"

    def get_initial(self):
        initial_values = super(UpdateProduct, self).get_initial()
        try:
            current_group = self.object.groups.get()
        except Exception as e:
            success_message = f"{e} Error Occured: Update form could not be preloaded"
            pass
        return initial_values

    def get_form_class(self):
        return ProductForm

    def get_success_url(self):
        return reverse('manage_site')


class DeleteProduct(SuccessMessageMixin, generic.DeleteView):
    model = Product
    success_message = 'Product Deleted!'
    template_name = "manage_site/product-delete.html"

    def get_success_url(self):
        return reverse('manage_site')

# CRUD for stock for admin area
