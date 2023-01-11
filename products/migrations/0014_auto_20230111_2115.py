# Generated by Django 3.2 on 2023-01-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20230110_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizestock',
            name='large',
        ),
        migrations.RemoveField(
            model_name='sizestock',
            name='medium',
        ),
        migrations.RemoveField(
            model_name='sizestock',
            name='small',
        ),
        migrations.RemoveField(
            model_name='sizestock',
            name='xlarge',
        ),
        migrations.RemoveField(
            model_name='sizestock',
            name='xsmall',
        ),
        migrations.AddField(
            model_name='sizestock',
            name='l',
            field=models.IntegerField(blank=True, null=True, verbose_name='large'),
        ),
        migrations.AddField(
            model_name='sizestock',
            name='m',
            field=models.IntegerField(blank=True, null=True, verbose_name='medium'),
        ),
        migrations.AddField(
            model_name='sizestock',
            name='s',
            field=models.IntegerField(blank=True, null=True, verbose_name='small'),
        ),
        migrations.AddField(
            model_name='sizestock',
            name='xl',
            field=models.IntegerField(blank=True, null=True, verbose_name='extra large'),
        ),
        migrations.AddField(
            model_name='sizestock',
            name='xs',
            field=models.IntegerField(blank=True, null=True, verbose_name='extra small'),
        ),
    ]