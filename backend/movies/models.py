from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    photo = models.URLField(max_length=1000)
    copies = models.IntegerField(default=0)