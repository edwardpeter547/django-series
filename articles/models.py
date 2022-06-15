from datetime import datetime
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.IntegerField()
    author = models.IntegerField()
    date_created = models.DateTimeField(default=datetime.utcnow)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now=False,null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
