from django import forms
from django.contrib.auth.models import User
from products.models import Product, SizeStock, RegularStock


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'desc', 'price', 'sale_price', 'image_url']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product Name *'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Slug (Auto loads if blank)'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Product description *', 'rows': 7}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price (£)'}),
            'sale_price': forms.NumberInput(attrs={'placeholder': 'Discount Price (£)'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
        }


class SizeStockForm(forms.ModelForm):
    class Meta:
        model = SizeStock
        fields = ['xs', 's', 'm', 'l', 'xl']

        widgets = {
            'xs': forms.NumberInput(attrs={'placeholder': 'XS'}),
            's': forms.NumberInput(attrs={'placeholder': 'S'}),
            'm': forms.NumberInput(attrs={'placeholder': 'M'}),
            'l': forms.NumberInput(attrs={'placeholder': 'L'}),
            'xl': forms.NumberInput(attrs={'placeholder': 'XL'}),
        }


class RegularStockForm(forms.ModelForm):
    class Meta:
        model = RegularStock
        fields = ['stock']

        widgets = {
            'stock': forms.NumberInput(attrs={'placeholder': 'Quantity'}),
        }

