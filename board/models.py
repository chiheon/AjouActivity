from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    company = models.CharField(max_length=100)
    date = models.CharField(max_length=1000)
    image = models.FileField(null=True, blank=True)
