from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def all_products(request):
    """ Displays products depending on categories selected """
    products = Product.objects.all()

    # Filters all clothing items
    if 'clothing' in request.GET:
        products = Product.objects.filter(category__name__in=[
            'jackets_coats',
            't-shirts',
            'fleeces_jumpers',
            'trousers',
            'socks'
            ])

    # Filters all gear items 
    if 'gear' in request.GET:
        products = Product.objects.filter(category__name__in=[
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

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """ Displays information about a single product """

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
