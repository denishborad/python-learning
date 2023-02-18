from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from loginn.models import UserRegister
from django.contrib.auth import authenticate, login


# Create your views here.
def Home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass1 = request.POST['pass']
        user = authenticate(request, username=user_name, password=pass1)
        if user is None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Login Required!!")

    return render(request,'login.html')

def Register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        sname = request.POST['sname']
        Email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            return HttpResponse('Your Password Is Not Right!!')
        else:
            my_user = User.objects.create_user(uname, sname, Email, pass1)
            my_user.save()
            return redirect('login')

                
    return render(request,'register.html')