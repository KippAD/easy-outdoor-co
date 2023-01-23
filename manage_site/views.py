from django.shortcuts import render, reverse
from products.models import Product, SizeStock, RegularStock
from checkout.models import Order
from profiles.models import UserProfile
from newsletter.models import MailingList
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from itertools import chain
from .forms import ProductForm, RegularStockForm, SizeStockForm


def manage_site(request):
    """Displays site management template for admin"""
    template = 'manage_site/manage-site.html'

    products = Product.objects.all()
    size_stock = SizeStock.objects.all()
    regular_stock = RegularStock.objects.all()
    orders = Order.objects.all()
    mailing_list = MailingList.objects.all()

    context = {
        'products': products,
        'regular_stock': regular_stock,
        'size_stock': size_stock,
        'orders': orders,
        'mailing_list': mailing_list,
    }

    return render(request, template, context)


# CRUD for products for admin area
class AddProduct(SuccessMessageMixin, generic.CreateView):
    """Creates product model"""
    model = Product
    form_class = ProductForm
    template_name = "manage_site/product-add.html"
    success_message = "Product Added!"

    def get_success_url(self):
        return reverse('manage-site')


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
        return reverse('manage-site')


class DeleteProduct(SuccessMessageMixin, generic.DeleteView):
    model = Product
    success_message = 'Product Deleted!'
    template_name = "manage_site/product-delete.html"

    def get_success_url(self):
        return reverse('manage-site')


# CRUD for stock for admin area
class UpdateSizeStock(SuccessMessageMixin, generic.UpdateView):
    """Updates product model"""
    model = SizeStock
    template_name = "manage_site/size-stock-update.html"
    fields = '__all__'
    success_message = "Product size stock updated!"

    def get_initial(self):
        initial_values = super(UpdateSizeStock, self).get_initial()
        try:
            current_group = self.object.groups.get()
        except Exception as e:
            success_message = f"{e} Error Occured: Update form could not be preloaded"
            pass
        return initial_values

    def get_form_class(self):
        return SizeStockForm

    def get_success_url(self):
        return reverse('manage-site')


class UpdateSizeStock(SuccessMessageMixin, generic.UpdateView):
    """Updates product model"""
    model = RegularStock
    template_name = "manage_site/regular-stock-update.html"
    fields = '__all__'
    success_message = "Product Stock Updated!"

    def get_initial(self):
        initial_values = super(UpdateSizeStock, self).get_initial()
        try:
            current_group = self.object.groups.get()
        except Exception as e:
            success_message = f"{e} Error Occured: Update form could not be preloaded"
            pass
        return initial_values

    def get_form_class(self):
        return RegularStockForm

    def get_success_url(self):
        return reverse('manage-site')


# View order details

class OrderDetails(SuccessMessageMixin, generic.DetailView):
    """Displays immutable order details"""
    model = Order
    template_name = "manage_site/order-detail.html"