# Generated by Django 3.2 on 2023-01-24 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_remove_regularstock_total_sold'),
        ('profiles', '0006_alter_productreview_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='products.product'),
        ),
    ]
