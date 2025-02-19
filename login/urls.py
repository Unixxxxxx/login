from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='index'),
    path('', include('myapp.urls')),
    path('', include('myapp1.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

