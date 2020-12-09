from django.db import models

# Create your models here.
class Alumno(models.Model):

    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    email = models.CharField(max_length=50)

    class Meta: 
        ordering = ['name']