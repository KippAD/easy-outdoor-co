from django.urls import path
from . import views

urlpatterns = [
    path("", views.manage_site, name="manage-site"),
    path("add-product/", views.AddProduct.as_view(), name="add-product"),
    path("update-product/<int:pk>", views.UpdateProduct.as_view(),
         name="update-product"),
    path("delete-product/<int:pk>", views.DeleteProduct.as_view(),
         name="delete-product"),
    path("update-size-stock/<int:pk>", views.UpdateSizeStock.as_view(),
         name="update-size-stock"),
    path("update-regular-stock/<int:pk>", views.UpdateRegularStock.as_view(),
         name="update-regular-stock"),
    path("order-details/<int:pk>", views.OrderDetails.as_view(),
         name="order-details"),
    path("update-profile/<int:user_id>", views.update_profile,
         name="update-profile"),
    path("delete-profile/<int:pk>", views.DeleteProfile.as_view(),
         name="delete-profile"),
    path("delete-email/<int:pk>", views.DeleteEmail.as_view(),
         name="delete-email"),
]
