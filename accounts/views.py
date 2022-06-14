from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def login_view(request):
    context = {}
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            return redirect("/")
        else:
            return render(request=request, template_name="accounts/login.html", context={"form": form})
    
    form = AuthenticationForm(request)    
    context.update({"form": form})
    return render(request=request, template_name="accounts/login.html", context=context)



def logout_view(request):
    
    if request.method == "POST":
        logout(request=request)
        redirect("/login/")
        
    context = {}
    return render(request=request, template_name="accounts/logout.html", context=context)

def register_view(request):
    
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/login/")
    context = {"form": form}
    return render(request=request, template_name="accounts/register.html", context=context)
