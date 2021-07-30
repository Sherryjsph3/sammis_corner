from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image_one  = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    image_two = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    blurb = RichTextField(blank=True, null=True)
    # blurb = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    