from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product, SizeStock, RegularStock


@receiver(post_save, sender=Product)
def create_size(sender, instance, created, **kwargs):
    if created:
        if instance.has_sizes is True:
            SizeStock.objects.create(
                product=instance,
            )
        else:
            RegularStock.objects.create(
                product=instance,
            )
