# Generated by Django 3.2 on 2023-01-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]