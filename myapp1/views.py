from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa  # For converting HTML to PDF
from .models import PdfFile 
from .models import BlogPost

def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def generate_pdf(request):
    # Query all PdfFile records
    pdf_files = PdfFile.objects.all()
    
    # Render a template to create the HTML content
    html = render_to_string('admin/pdf_list.html', {'pdf_files': pdf_files})
    
    # Create the response object with content type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdf_files_list.pdf"'
    
    # Convert HTML to PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    # Return the PDF
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=400)
    return response
