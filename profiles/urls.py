from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order-history', views.order_history, name='order-history'),
    path('rating-form/<int:product_id>', views.load_rating_form, name='load-rating-form'),
    path('rate-product/<int:product_id>', views.rate_product, name='rate-product'),
]
