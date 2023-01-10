# Generated by Django 3.2 on 2023-01-10 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20230110_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xsmall', models.IntegerField(blank=True, null=True)),
                ('small', models.IntegerField(blank=True, null=True)),
                ('medium', models.IntegerField(blank=True, null=True)),
                ('large', models.IntegerField(blank=True, null=True)),
                ('xlarge', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_stock', to='products.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='productstock',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productstock',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='ProductStock',
        ),
    ]