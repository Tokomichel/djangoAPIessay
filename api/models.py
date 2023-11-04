from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=40)
    date = models.DateField()
