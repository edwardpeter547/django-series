from django.contrib import admin

# import models
from . models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date_created', 'timestamp', 'published']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
