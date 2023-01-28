from products.models import Product
from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for product_id, product_data in basket.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            basket_items.append({
                "product_id": product_id,
                "quantity": product_data,
                "product": product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size_selection, quantity in product_data[
                    "size_quantities"].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    "product_id": product_id,
                    "quantity": quantity,
                    "product": product,
                    "size_selection": size_selection,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "basket_items": basket_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "grand_total": grand_total,
    }

    return context
