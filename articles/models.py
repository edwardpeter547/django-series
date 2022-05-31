from datetime import datetime
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    category = models.IntegerField()
    author = models.IntegerField()
    date_created = models.DateTimeField(default=datetime.utcnow)
