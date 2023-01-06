from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def riendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    desc = models.TextField()
    sizes = models.BooleanField(null=True, blank=True, default=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    total_sold = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
