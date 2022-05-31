# django related imports
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# project file imports
from . models import Article

# Create your views here.

# Todo: view to create a new article
@login_required
def create_view(request):
    
    context = {}
    
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        category = request.POST.get("category")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, author=author, category=category, content=content)
        context["artcle"] = article
        context["created"] = True
    
    return render(request=request, template_name="articles/create.html", context=context)


# Todo: create a search view.
def search_view(request):
    
    request_data = request.GET.get('search')

    try:
        query = int(request_data)
    except:
        query = None
        
    article = None
        
    if query is not None:
        article = Article.objects.get(id=query)
    
    context = {'article': article}
    return render(request=request, template_name="articles/search.html", context=context)


# Todo create a view to view article details.
def detail_view(request, id=None):
    
    article = None
    
    if id is not None:
        article = Article.objects.get(id=id)
    
    context = {
        "article": article
    }
    
    
    return render(request=request,template_name="articles/detail.html", context=context)
