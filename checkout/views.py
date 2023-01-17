from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is currently empty")
        return redirect(reverse('products'))

        order_form = OrderForm()
        context = {
            'order_form': order_form,
        }

        return render(request, 'checkout/checkout.html', context)