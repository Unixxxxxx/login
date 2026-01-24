from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    
    path('myapp/', include('myapp.urls')),     
    path('myapp1/', include('myapp1.urls')),
    path('form/', include("form.urls")),
]   

# Serve static & media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler404 = 'login.views.custom_page_not_found'
