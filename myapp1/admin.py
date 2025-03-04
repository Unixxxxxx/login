from django.contrib import admin
import csv
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import UserFormData
from .models import BlogPost, PdfFile

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # You can customize the columns shown in the list view
    search_fields = ('title',)  # Allows searching by title

admin.site.register(BlogPost, BlogPostAdmin)

# Define the export action
def export_to_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_form_data.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['Name', 'Email', 'Message', 'Created At'])

    # Write data rows
    for obj in queryset:
        writer.writerow([obj.name, obj.email, obj.message, obj.created_at])

    return response

# Give the action a nice name in the admin
export_to_csv.short_description = "Export selected data to CSV"

# Register the model in admin
@admin.register(UserFormData)
class UserFormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')  # Columns to display
    actions = [export_to_csv]  # Add the export action

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
