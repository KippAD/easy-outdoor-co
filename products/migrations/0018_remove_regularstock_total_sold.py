# Generated by Django 3.2 on 2023-01-20 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularstock',
            name='total_sold',
        ),
    ]
