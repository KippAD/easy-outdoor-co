from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_site, name='manage_site'),
    path('add-product/', views.AddProduct.as_view(), name='add-product'),
]
