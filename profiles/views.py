from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Avg
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from .models import UserProfile, ProductReview
from checkout.models import Order, OrderLineItem
from products.models import Product
from .forms import UserProfileForm, UserDeliveryForm, ProductReviewForm
from django.contrib import messages
from django.forms.models import model_to_dict


def profile(request):
    """ Display user profiles """
    user = request.user
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        user_form = UserProfileForm(request.POST, instance=user)
        delivery_form = UserDeliveryForm(request.POST, instance=profile)
        if delivery_form.is_valid() and user_form.is_valid():
            user_form.save()
            delivery_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect(reverse("profile"))
        else:
            messages.error(
                request,
                "Update failed. Please ensure the form is valid."
                )
    else:
        user_form = UserProfileForm(instance=user)
        delivery_form = UserDeliveryForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "user": user,
        "profile": profile,
        "user_form": user_form,
        "delivery_form": delivery_form,
    }

    return render(request, template, context)


def order_history(request):
    """ Display user's order history """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile)
    ordered_orders = orders.order_by('-date')
    user = request.user
    reviews = ProductReview.objects.filter(user=user)

    template = "profiles/order_history.html"
    context = {
        "orders": ordered_orders,
        "reviews": reviews,
    }

    return render(request, template, context)


def load_rating_form(request, product_id):
    """Loads form for user to leave a rating"""
    product = get_object_or_404(Product, id=product_id)
    rating_form = ProductReviewForm()
    template = "profiles/rate-product.html"
    context = {
        "form": rating_form,
        "product": product,
    }
    return render(request, template, context)


def rate_product(request, product_id):
    """Handles and submits rating"""
    product = get_object_or_404(Product, id=product_id)
    rating_form = ProductReviewForm(data=request.POST)
    user = request.user
    rating = request.POST.get("rating")
    if not rating:
        rating = 0
    else:
        rating = rating
    try:
        if rating_form.is_valid():
            rating_form.instance.user = user
            rating_form.instance.product = product
            rating_form.instance.rating = rating
            rating_form.instance.comment = request.POST.get("comment")
            rating_form.save()
            # Sets product rating to average of all ratings
            product_ratings = ProductReview.objects.filter(product=product)
            average_rating = product_ratings.aggregate(
                Avg("rating"))["rating__avg"]
            product.rating = round(average_rating, 2)
            product.save()
            messages.success(request, f"Product Rated {rating} stars! \
                Thank you for your feedback.")
        else:
            messages.error(request, "The form was invalid and could \
                 not be processed. Please try again.")
            rating_form = ProductReviewForm()

    except IntegrityError:
        messages.error(
            request,
            "Error: You have already reviewed this product."
            )

    return redirect("order-history")
