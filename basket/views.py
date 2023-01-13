from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, SizeStock


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
            else:
                basket[product_id]['size_quantities'][size_selection] = quantity
        else:
            basket[product_id] = {'size_quantities': {size_selection: quantity}}
    else:
        if product_id in list(basket.keys()):
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity

    print(basket)

    request.session['basket'] = basket

    return redirect(redirect_url)


def update_quantity(request, product_id):
    basket = request.session.get('basket', {})
    print(basket)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    if 'product_size' in request.POST:
        size_selection = request.POST.get('product_size')
        print(size_selection)

    if size_selection:
        if 'increment' in request.POST:
            basket[product_id]['size_quantities'][size_selection] += 1
            print(basket)
        elif 'decrement' in request.POST:
            basket[product_id]['size_quantities'][size_selection] -= 1
            print(basket)

    request.session['basket'] = basket
    return render(request, "basket/basket.html")