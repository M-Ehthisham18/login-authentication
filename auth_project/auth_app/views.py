from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import  HttpResponse

# Create your views here.

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
    return render(request, 'login_page.html')   

def dashborder(request):
    return render(request, 'dashborder.html')   