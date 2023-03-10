# Generated by Django 3.2 on 2023-01-09 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230109_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstock',
            name='product_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='products.productstock'),
        ),
    ]
