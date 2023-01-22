from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_site, name='manage-site'),
    path('add-product/', views.AddProduct.as_view(), name='add-product'),
    path('update-product/<int:pk>', views.UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<int:pk>>', views.DeleteProduct.as_view(), name='delete-product'),
    path('update-size-stock/<int:pk>>', views.UpdateSizeStock.as_view(), name='update-size-stock'),
    path('update-regular-stock/<int:pk>>', views.UpdateSizeStock.as_view(), name='update-regular-stock'),
]
