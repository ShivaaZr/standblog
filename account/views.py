from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout



def user_login(request):
    if request.user.is_authenticated == "True":
        return redirect('/')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home_app:main")
        
        
    return render(request, "account\login.html", {})


def user_register(request):
    context = {'errors' :[]}
    if request.user.is_authenticated == "True":
        return redirect('home_app:main')
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            context['errors'].append('passwords are not match.')
            return render(request, "account/register.html", context)
        
        
        user = User.objects.create(username = username, email=email, password= password1)
        login(request, user)
        return redirect('home_app:main')
        
    return render(request, "account/register.html", {})


def user_logout(request):
    logout(request)
    return redirect('home_app:main')



    


    
