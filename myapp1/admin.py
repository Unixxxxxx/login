from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # You can customize the columns shown in the list view
    search_fields = ('title',)  # Allows searching by title

admin.site.register(BlogPost, BlogPostAdmin)
