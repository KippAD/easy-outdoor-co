from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from profiles.forms import UserDeliveryForm
from products.models import Product, SizeStock, RegularStock
from basket.contexts import basket_contents

import stripe
import json

# Views taken from Boutiqe Ado walkthrough projcect by CodeInstitue
@require_POST
def cache_checkout_data(request):
    try:
        username = request.user
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Your payment was unsuccessfully \
            processed. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for product_id, product_data in basket.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                        order_line_item.save()
                        # Updates stock with quantity
                        regular_stock = get_object_or_404(RegularStock, product=product)         
                        if (regular_stock.stock - product_data) >= 0:
                            updated_stock = (regular_stock.stock - product_data)
                            setattr(regular_stock, "stock", updated_stock)
                            regular_stock.save()
                        else:
                            messages.error(request, (
                                f"Unfortunately we only have {regular_stock.stock} left of the {product}. "
                                "Please update the quantity or remove the item to complete your order!")
                            )
                            return redirect(reverse('view_basket'))
                    else:
                        for size, quantity in product_data['size_quantities'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                            # Updates stock with quantity
                            item_stock = get_object_or_404(SizeStock, product=product)
                            size_stock = getattr(item_stock, size)
                            if (size_stock - quantity) >= 0:
                                updated_stock = (size_stock - quantity)
                                setattr(item_stock, size, updated_stock)
                                item_stock.save()
                            else:
                                messages.error(request, (
                                    f"Unfortunately we only have {size_stock} left of the {product} in {product_size}. "
                                    "Please update the quantity, choose another size, or remove the item from the basket to complete your order!")
                                )
                                return redirect(reverse('view_basket'))

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))
            # For saving information to profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please try again.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your basket is currently empty.")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Prefills checkout form with user saved information
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts and redirects to success page
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    order_items = OrderLineItem.objects.filter(order=order)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
        # Save the user's info
        if save_info:

            delivery_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserDeliveryForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Thank you, your order has been successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_items': order_items,
    }

    return render(request, template, context)