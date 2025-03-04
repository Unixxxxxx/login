from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.lname}"

class PdfFile(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdf_files/')  # This will store PDFs in MEDIA_ROOT/pdf_files
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
