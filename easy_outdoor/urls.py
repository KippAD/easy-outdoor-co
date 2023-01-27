from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('manage/', include('manage_site.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('summernote/', include('django_summernote.urls')),
]

handler404 = "easy_outdoor.views.page_not_found_view"
handler403 = "easy_outdoor.views.page_forbidden_found_view"
handler500 = "easy_outdoor.views.server_error_view"