from django.urls import path 
from .views import app0

urlpatterns = [
        path('', app0, name='app0'),
        ]
