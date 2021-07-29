from django.db import models
from django.db.models.base import Model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image_one  = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    image_two = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    blurb = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    