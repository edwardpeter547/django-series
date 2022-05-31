# python related imports
from datetime import datetime

# django related imports
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# models related imports
from articles.models import Article

article = Article.objects.get(id=2)
artile_list = Article.objects.all()

context = {
    "object_list": artile_list,
    "title": article.title,
    "id": article.id,
    "content": article.content,
    "datecreated": article.date_created.strftime("%dth, %B %Y")
}


def home_view(request, id = None):
    
    HTML_STRING = render_to_string("home-view.html", context=context)
    """Take in a request and retun HTML as response"""
    
    return HttpResponse(HTML_STRING)
    
    
    
    