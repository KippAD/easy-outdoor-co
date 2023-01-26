from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from products.models import Product
from django.core.validators import MaxValueValidator


class UserProfile(models.Model):
    """
    Model that stores users personal and delivery
    information for future deliveries
    """
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or updates the profile of the user
    """
    if created:
        UserProfile.objects.create(user=instance)
    # If user exists then save the profile
    instance.userprofile.save()


class ProductReview(models.Model):
    """Model to store user reviews"""
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name="product_reviews", on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, validators=[MaxValueValidator(5)])
    comment = models.TextField(max_length=400, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product',)