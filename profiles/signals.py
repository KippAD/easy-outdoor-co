from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .models import ProductReview
from products.models import Product
from statistics import mean


@receiver(post_save, sender=ProductReview)
def set_product_rating(sender, instance, created, **kwargs):
    product = get_object_or_404(Product, id=instance.product.id)
    print(product)
    product_ratings = ProductReview.objects.filter(product=product)
    print(product_ratings)
    ratings = []
    for r in product_ratings:
        ratings.append(r.rating)

    product.rating = mean(ratings)
    product.save()
