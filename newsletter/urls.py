from django.urls import path
from . import views

urlpatterns = [
    path('mailing-list', views.newsletter_subscribe, name='mailing-list'),
]
