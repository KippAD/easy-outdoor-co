from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product, SizeStock, RegularStock
from django.contrib import messages
from django.http import HttpResponseRedirect
from basket.contexts import basket_contents


def view_basket(request):

    return render(request, "basket/basket.html")


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size_selection = None

    basket = request.session.get('basket', {})

    if product.has_sizes:
        size_selection = request.POST.get('sizes').lower()
        # Ensures that users can't add more stock to basket than is available
        item_stock = get_object_or_404(SizeStock, product=product)
        size_stock = getattr(item_stock, size_selection)

        if (size_stock - quantity) >= 0:
            if product_id in list(basket.keys()):
                if size_selection in basket[product_id]['size_quantities'].keys():
                    if (basket[product_id]['size_quantities'][size_selection] + quantity) <= size_stock:
                        basket[product_id]['size_quantities'][size_selection] += quantity
                        messages.success(request, f'Added {quantity} {product.name} in size 1 {size_selection.upper()} to the basket')
                    else:
                        messages.error(request, (
                            f"You have already added {quantity} of {product} to your basket. "
                            "This is all of our remaining stock.")
                            )
                else:
                    basket[product_id]['size_quantities'][size_selection] = quantity
                    messages.success(request, f'Added {quantity} {product.name} in size 2 {size_selection.upper()} to the basket')
            else:
                basket[product_id] = {'size_quantities': {size_selection: quantity}}
                messages.success(request, f'Added {quantity} {product.name} in size 3{size_selection.upper()} to the basket')
        else:
            messages.error(request, (
                f"We're sorry! We only have {quantity} left of the {product} in {size_selection}. "
                "Check to see if the remaining items are already in your basket.")
                )
    else:
        regular_stock = get_object_or_404(RegularStock, product=product)         
        if (regular_stock.stock - quantity) >= 0:
            if product_id in list(basket.keys()):
                if (basket[product_id] + quantity) <= regular_stock.stock:
                    basket[product_id] += quantity
                    messages.success(request, f'Added {product.name} to the basket')
                else:
                    messages.error(request, (
                        f"You have already added {quantity} of {product} to your basket. "
                        "This is all of our remaining stock.")
                        )
            else:
                basket[product_id] = quantity
                messages.success(request, f'Added {product.name} to the basket')
        else:
            messages.error(request, (
                f"We're sorry! We only have {quantity} left of the {product}. "
                "Check to see if the remaining items are already in your basket.")
                )

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
    print(basket)
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


# Check stock function

def check_size_stock(basket, product, stock_type, quantity, size):
    """Function to ensure that size stocks caan't be exceeded"""
    available = None
    item_stock = get_object_or_404(SizeStock, product=product)
    size_stock = getattr(item_stock, size)
    product_id = str(product.id)

    if product_id in basket.keys():
        if basket[product_id]['size_quantities'][size] >= size_stock:
            available = False
    else:
        if (size_stock - quantity) < 0:
            available = False
        else:
            available = True

    return available



