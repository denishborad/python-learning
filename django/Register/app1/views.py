from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from app1.models import sign_up
from django.contrib.auth import authenticate,login

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        pass1 = request.POST['pass']
        user = authenticate(request, uname=username, password=pass1)
        print("Hello",user)
        if user is None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Login Required!')

    return render(request, 'login.html')

def Signup(request):
    if request.method == 'POST':
        user_name = request.POST['uname']
        Email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            return HttpResponse('Your Password Is Wrong!')
        else:
            my_user = sign_up(user_name=user_name,Email=Email,pass1=pass1)
            my_user.save()
            myuser = User.objects.create_user(user_name,Email,pass1)
            myuser.save()
            return redirect('login')
        # print(user_name=user_name,Email,pass1,pass2)
    return render(request, 'signup.html') 