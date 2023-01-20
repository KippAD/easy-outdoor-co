from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm, UserDeliveryForm
from django.contrib import messages


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
