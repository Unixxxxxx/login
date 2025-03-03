from django.contrib import admin
from .models import User
from .models import PdfFile

admin.site.register(User)
# Register your models here.

class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pdf_file')  # Display fields in the list view
    search_fields = ('title', 'description')  # Allow search by title or description

# Register the model with the admin interface
admin.site.register(PdfFile, PdfFileAdmin)