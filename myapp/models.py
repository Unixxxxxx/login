from django.db import models
class Form(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=50, null=True)
    age= models.IntegerField(null=True)


    def __str__(self):
        return self.name 
# Create your models here.
