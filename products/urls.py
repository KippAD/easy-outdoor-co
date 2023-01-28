from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<slug:slug>/", views.product_detail, name="product-detail"),
    path("<slug:slug>/reviews", views.product_reviews, name="product-reviews"),
]
