from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.db.models.functions import Lower


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

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """ Displays information about a single product """

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
