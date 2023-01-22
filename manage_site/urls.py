from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_site, name='manage-site'),
    path('add-product/', views.AddProduct.as_view(), name='add-product'),
    path('update/<int:pk>', views.UpdateProduct.as_view(), name='update-product'),
    path('delete/<int:pk>>', views.DeleteProduct.as_view(), name='delete-product'),
]
