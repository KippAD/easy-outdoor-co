from django.shortcuts import render, reverse, get_object_or_404, redirect
from products.models import Product, SizeStock, RegularStock
from checkout.models import Order
from profiles.models import UserProfile
from newsletter.models import MailingList
from profiles.forms import UserDeliveryForm, UserProfileForm
from .forms import ProductForm, RegularStockForm, SizeStockForm

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from django import forms
from itertools import chain


@user_passes_test(lambda user: user.is_staff)
def manage_site(request):
    """Displays site management template for admin"""
    template = "manage_site/manage-site.html"

    products = Product.objects.all()
    size_stock = SizeStock.objects.all()
    regular_stock = RegularStock.objects.all()
    orders = Order.objects.all()
    mailing_list = MailingList.objects.all()
    profiles = UserProfile.objects.all()

    context = {
        "products": products,
        "regular_stock": regular_stock,
        "size_stock": size_stock,
        "orders": orders,
        "mailing_list": mailing_list,
        "profiles": profiles,
    }

    return render(request, template, context)


# CRUD for products for admin area
class AddProduct(SuccessMessageMixin, UserPassesTestMixin, generic.CreateView):
    """Creates product model"""
    model = Product
    form_class = ProductForm
    template_name = "manage_site/product-add.html"
    success_message = "Product Added!"

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")


class UpdateProduct(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    """Updates product model"""
    model = Product
    template_name = "manage_site/product-update.html"
    fields = "__all__"
    success_message = "Product Updated!"

    def get_initial(self):
        initial_values = super(UpdateProduct, self).get_initial()
        return initial_values

    def get_form_class(self):
        return ProductForm

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")


class DeleteProduct(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Product
    delete_message = "Product Deleted!"
    template_name = "manage_site/product-delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.delete_message)
        return super(DeleteProfile, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")


# CRUD for stock for admin area
class UpdateSizeStock(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    """Updates product model"""
    model = SizeStock
    template_name = "manage_site/size-stock-update.html"
    fields = "__all__"
    success_message = "Product size stock updated!"

    def get_initial(self):
        initial_values = super(UpdateSizeStock, self).get_initial()
        return initial_values

    def get_form_class(self):
        return SizeStockForm

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")


class UpdateRegularStock(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    """Updates product model"""
    model = RegularStock
    template_name = "manage_site/regular-stock-update.html"
    success_message = "Product Stock Updated!"

    def get_initial(self):
        initial_values = super().get_initial()
        return initial_values

    def get_form_class(self):
        return RegularStockForm

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")


# View order details
class OrderDetails(SuccessMessageMixin, UserPassesTestMixin, DetailView):
    """Displays immutable order details"""
    model = Order
    template_name = "manage_site/order-detail.html"

    def test_func(self):
        return self.request.user.is_staff


# Crud for users
@user_passes_test(lambda user: user.is_staff)
def update_profile(request, user_id):
    """ Displays form and updates users information """
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        user_form = UserProfileForm(request.POST, instance=user)
        delivery_form = UserDeliveryForm(request.POST, instance=profile)
        if delivery_form.is_valid() and user_form.is_valid():
            user_form.save()
            delivery_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect(reverse("manage-site"))
        else:
            messages.error(
                request,
                "Update failed. Please ensure the form is valid."
                )
            raise ValidationError(
                    f"Your form was not updated, please fill out \
                    the form correctly."
                )
    else:
        user_form = UserProfileForm(instance=user)
        delivery_form = UserDeliveryForm(instance=profile)
    orders = profile.orders.all()

    template = "manage_site/profile-update.html"
    context = {
        "user": user,
        "profile": profile,
        "user_form": user_form,
        "delivery_form": delivery_form,
    }

    return render(request, template, context)


class DeleteProfile(UserPassesTestMixin, generic.DeleteView):
    """Deletes user profile from the database"""
    model = User
    delete_message = "User Deleted!"
    template_name = "manage_site/profile-delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.delete_message)
        return super(DeleteProfile, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")


# Delete email from newsletter database
class DeleteEmail(UserPassesTestMixin, DeleteView):
    """Deletes user profile from the database"""
    model = MailingList
    delete_message = "Email removed from mailing list!"
    template_name = "manage_site/email-delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.delete_message)
        return super(DeleteEmail, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse("manage-site")
