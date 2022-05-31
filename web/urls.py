"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import (detail_view, search_view, create_view)
from accounts.views import (register_view, login_view, logout_view)

urlpatterns = [
    # admin routes
    path('admin/', admin.site.urls),
    
    # account routes
    path('login/', login_view),
    path('logout/', logout_view),
    
    # home routes
    path('', home_view),
    
    # article routes
    path('articles/', search_view),
    path('articles/create', create_view),
    path('articles/<int:id>', detail_view)
]
