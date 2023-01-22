from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history', views.order_history, name='order_history'),
    path('mailing-list', views.mailing_list, name='mailing-list'),
]
