from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_basket, name="view_basket"),
    path("add/<product_id>/", views.add_to_basket, name="add_to_basket"),
    path("update/<product_id>/", views.update_quantity, name="update_quantity"),
    path("delete/<product_id>/", views.delete_item, name="delete_item"),
]
