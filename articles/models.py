from datetime import datetime
from django.db import models
from django.utils import timezone

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
