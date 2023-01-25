from django.urls import path
from . import views

urlpatterns = [
    path('mailing-list', views.newsletter_subscribe, name='mailing-list'),
    path('newsletter-form', views.newsletter_form, name='newsletter-form'),
    path('send-newsletter', views.send_newsletter, name='send-newsletter'),
    path('contact-form', views.contact_form, name='contact-form'),
]
