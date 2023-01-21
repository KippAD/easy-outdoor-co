# from django import forms
# from django.contrib.auth.models import User
# from products.models import Product


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         """
#         Add placeholders and classes, remove auto-generated
#         labels and set autofocus on first field
#         """
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'name': 'Product Name',
#             'desc': 'Description',
#             'slug': 'Slug (Auto-Completes if blank)',
#         }

#         for field in self.fields:
#             if self.fields[field].required:
#                 placeholder = f'{placeholders[field]} *'
#             else:
#                 placeholder = placeholders[field]
#             self.fields[field].widget.attrs['placeholder'] = placeholder
#             self.fields[field].label = False
