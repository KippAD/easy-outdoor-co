from django.shortcuts import render, get_object_or_404, redirect
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

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        delivery_form = UserDeliveryForm(request.POST, instance=profile)
        if delivery_form.is_valid() and user_form.is_valid():
            user_form.save()
            delivery_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        user_form = UserProfileForm(instance=user)
        delivery_form = UserDeliveryForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'user': user,
        'profile': profile,
        'user_form': user_form,
        'delivery_form': delivery_form,
    }

    return render(request, template, context)


def order_history(request):
    """ Display user's order history' """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile)
    user = request.user
    reviews = ProductReview.objects.filter(user=user)

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
        'reviews': reviews,
    }

    return render(request, template, context)


def load_rating_form(request, product_id):
    """Loads form for user to leave a rating"""
    product = get_object_or_404(Product, id=product_id)
    rating_form = ProductReviewForm()
    template = 'profiles/product-review.html'
    context = {
        'form': rating_form,
        'product': product,
    }
    return render(request, template, context)


def rate_product(request, product_id):
    """Handles and submits rating"""
    product = get_object_or_404(Product, id=product_id)
    rating_form = ProductReviewForm(data=request.POST)
    if rating_form.is_valid():
        rating_form.instance.user = request.user
        rating_form.instance.product = product
        rating_form.instance.rating = request.POST.get('rating')
        rating_form.instance.comment = request.POST.get('comment')
        rating_form.save()
    else:
        rating_form = CommentForm()

    messages.success(request, 'Product Rated! Thank you for your feedback.')
    return redirect('order-history')
