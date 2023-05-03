from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    remarks = RichTextField()
    
