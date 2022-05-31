from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    context = {}
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request=request, username = username, password = password)
        if not user:
            context["error"] = "username or password is incorrect"
            return render(request=request, template_name="accounts/login.html", context=context)
        login(request=request, user=user)
        return redirect("/")
    
    return render(request=request, template_name="accounts/login.html", context=context)

def logout_view(request):
    
    if request.method == "POST":
        logout(request=request)
        redirect("/login/")
        
    context = {}
    return render(request=request, template_name="accounts/logout.html", context=context)

def register_view(request):
    context = {}
    return render(request=request, template_name="accounts/register.html", context=context)
