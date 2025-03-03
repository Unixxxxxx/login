from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PdfFile(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdf_files/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

