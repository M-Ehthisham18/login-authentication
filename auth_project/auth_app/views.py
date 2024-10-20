from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login_page')
def dashborder(request):
    user_name = request.user
    return render(request, 'dashborder.html',{'user_name':user_name})  

def register_page(request):
    if request.method == 'POST':
        user_name =  request.POST.get('user_name')
        email =  request.POST.get('email')
        pass1 =  request.POST.get('pass1')
        pass2 =  request.POST.get('pass2')
        
        if User.objects.filter(email=email).exists():
                return HttpResponse("<h2>email already exists.</h2>")
        
        if pass1 == pass2:
            my_user = User.objects.create_user(user_name,email,pass1)
            my_user.save()
        else:
            return HttpResponse("Passwords do not match.")
        return redirect ('dashborder')
    
    return render(request, 'register_page.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('Email or Password is incorrect')

        # Authenticate using the username (since Django requires username)
        user = authenticate(request, username=user.username, password=pass1)
        print (user)
        if user is not None:
            login(request,user)
            return redirect('dashborder')
        else:
            return HttpResponse('email or Password is incorrect')
        
    return render(request, 'login_page.html')   

def logout_page(request):
    logout(request)
    return redirect('login_page')