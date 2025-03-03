from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost, PdfFile

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # You can customize the columns shown in the list view
    search_fields = ('title',)  # Allows searching by title

admin.site.register(BlogPost, BlogPostAdmin)

class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pdf_file')
    
    # Add a custom action for PDF generation
    def download_pdf(self, request, queryset):
        # URL to the PDF generation view
        url = reverse('generate_pdf')
        return HttpResponseRedirect(url)
    
    download_pdf.short_description = 'Download All PDFs as PDF'
    actions = [download_pdf]  # Register the action

admin.site.register(PdfFile, PdfFileAdmin)
