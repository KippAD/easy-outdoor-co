from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category, SizeStock, RegularStock
from django.db.models import Q, Min, Max
from django.db.models.functions import Lower
from django.forms.models import model_to_dict
from django.contrib import messages
import random


def all_products(request):
    """ Displays products depending on categories selected """
    products = Product.objects.all()
    search = None
    sort = None
    direction = None

    if request.GET:

        # Filters all clothing items
        if 'clothing' in request.GET:
            products = products.filter(category__name__in=[
                'jackets_coats',
                't-shirts',
                'fleeces_jumpers',
                'trousers',
                'socks'
                ])

        # Filters all gear items 
        if 'gear' in request.GET:
            products = products.filter(category__name__in=[
                'gloves',
                'headwear',
                'equipment',
                'footwear',
                'sunglasses'
                ])

        # Filters specific category types
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)

        # Search functionality
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "The search query was empty.")
                return redirect(reverse('products'))

            searches = Q(name__icontains=search) | Q(desc__icontains=search)
            products = products.filter(searches)

        #  Sorting method taken from Code Institute Boutique Ado walkthrough project
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Sale functionality
        if 'sale' in request.GET:
            products = Product.objects.filter(sale_price__gt=0)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """ Displays information about a single product """
    product = get_object_or_404(Product, slug=slug)

    if product.has_sizes:
        product_sizes = get_object_or_404(SizeStock, product=product)
        # Converts sizes into dictionary and removes non size attributes
        product_sizes = model_to_dict(product_sizes)
        del_keys = ['id', 'product']
        for key in del_keys:
            del product_sizes[key]

        sizes = {k.upper(): v for k, v in product_sizes.items()}
        # Checks if stock exists accross all sizes
        if all(value == None or value == 0 for value in product_sizes.values()):
            stock = None
        else:
            stock = list(product_sizes.values())
        
    else:
        # Checks if stock exists on item
        sizes = None
        product_stock = get_object_or_404(RegularStock, product=product)
        stock = product_stock.stock

    related_products = list(Product.objects.filter(category=product.category))
    product_count = len(related_products)

    if product_count > 8:
        random_products = random.sample(related_products, k=8)
    else:
        random_products = random.sample(related_products, len(related_products))

    # For toast to know where message is coming from
    add_basket = True

    context = {
        'product': product,
        'sizes': sizes,
        'stock': stock,
        'related_products': random_products,
        'add_basket': add_basket,
    }

    return render(request, 'products/product-detail.html', context)


def product_reviews(request, slug):
    """Displays reviews of specific product"""
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product-reviews.html', context)