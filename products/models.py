from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator


class Category(models.Model):
    """Model to store categories for the product model"""
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.friendly_name:
            self.friendly_name = self.name.capitalize()
        return super().save(*args, **kwargs)


class Product(models.Model):
    """Model to store product information and characteristics"""
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    has_sizes = models.BooleanField(blank=False, default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, validators=[MaxValueValidator(5)])
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    # Auto generates the slugfield
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    # Rounds to nearest .5 for the star rating
    def round_rating(self):
        return round(self.rating * 2) / 2


class SizeStock(models.Model):
    """Model to keep stock of products with sizes"""
    product = models.ForeignKey('Product', related_name="size_stock", on_delete=models.CASCADE)
    xs = models.IntegerField('extra small', null=True, blank=True)
    s = models.IntegerField('small', null=True, blank=True)
    m = models.IntegerField('medium', null=True, blank=True)
    l = models.IntegerField('large', null=True, blank=True)
    xl = models.IntegerField('extra large', null=True, blank=True)
    
    def __str__(self):
        return self.product + "Size Stock"


class RegularStock(models.Model):
    """Model to keep stock of products without sizes"""
    product = models.ForeignKey('Product', related_name="regular_stock", on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product + "Regular Stock"