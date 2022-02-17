from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login


#user-S@n@t,password-django123
# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        
        #check if user has entered correct username and password
        user = authenticate(username= username, password=password)
        
        if  user is not None:
            login(request,user)

        # A backend authenticated the credentials #approved
            return redirect("/")        #redirected to homepage
        else:
             return render(request, 'login.html')
            # No backend authenticated the credentials #not approved

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")


