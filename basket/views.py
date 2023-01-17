from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product, SizeStock
from django.contrib import messages
from django.http import HttpResponseRedirect


def view_basket(request):

    return render(request, "basket/basket.html")


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    quantity = int(request.POST.get('quantity'))
    print(quantity)
    redirect_url = request.POST.get('redirect_url')
    size_selection = None

    basket = request.session.get('basket', {})

    if product.has_sizes:
        size_selection = request.POST.get('sizes').lower()
        if product_id in list(basket.keys()):
            if size_selection in basket[product_id]['size_quantities'].keys():
                basket[product_id]['size_quantities'][size_selection] += quantity
                messages.success(request, f'Added {quantity} {product.name} in size {size_selection.upper()} to the basket')
            else:
                basket[product_id]['size_quantities'][size_selection] = quantity
                messages.success(request, f'Added {quantity} {product.name} in size {size_selection.upper()} to the basket')
        else:
            basket[product_id] = {'size_quantities': {size_selection: quantity}}
            messages.success(request, f'Added {quantity} {product.name} in size {size_selection.upper()} to the basket')
    else:
        if product_id in list(basket.keys()):
            basket[product_id] += quantity
            messages.success(request, f'Added {product.name} to the basket')
        else:
            basket[product_id] = quantity
            messages.success(request, f'Added {product.name} to the basket')

    print(basket)
    request.session['basket'] = basket
    return redirect(redirect_url)


def update_quantity(request, product_id):
    basket = request.session.get('basket', {})
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url')
    size_selection = None
    if 'product_size' in request.POST:
        size_selection = request.POST.get('product_size')
        print(size_selection)

    if size_selection:
        if 'increment' in request.POST:
            basket[product_id]['size_quantities'][size_selection] += 1
            messages.success(request, f'Changed {product.name} quantity')
        elif 'decrement' in request.POST:
            if basket[product_id]['size_quantities'][size_selection] > 1:
                basket[product_id]['size_quantities'][size_selection] -= 1
                messages.success(request, f'Changed {product.name} quantity')
            else:
                del basket[product_id]['size_quantities'][size_selection]
                messages.success(request, f'Removed {product.name} in size {size_selection.upper()} from the basket')
    else:
        if 'increment' in request.POST:
            basket[product_id] += 1
            messages.success(request, f'Changed {product.name} quantity')
        elif 'decrement' in request.POST:
            if basket[product_id] > 1:
                basket[product_id] -= 1
                messages.success(request, f'Changed {product.name} quantity')
            else:
                basket.pop(product_id)
                messages.success(request, f'Removed {product.name} from the basket')

    request.session['basket'] = basket
    return redirect(redirect_url, status=200)


def delete_item(request, product_id):

    try:
        product = get_object_or_404(Product, pk=product_id)
        size_selection = None
        if 'product_size' in request.POST:
            size_selection = request.POST.get('product_size')

        basket = request.session.get('basket', {})

        if size_selection:
            del basket[product_id]['size_quantities'][size_selection]
            messages.success(request, f'Removed {product.name} in size {size_selection.upper()} from the basket')
        else:
            basket.pop(product_id)
            messages.success(request, f'Removed {product.name} from the basket')

        request.session['basket'] = basket
        return render(request, "basket/basket.html", status=200)

    except Exception as e:
        messages.error(request, f'Error removing item from shopping basket: {e}')
        return HttpResponse(status=500)