from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_posts, name='blog_posts'),
]
