# Generated by Django 3.2 on 2023-01-18 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]