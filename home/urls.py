from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="home"),
    path("frequently-asked/", views.frequently_asked_questions,
         name="frequently-asked-questions"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
