from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = RichTextField()
    author = models.ForeignKey(User)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, blank=True)
