from Authentication import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render (request, "application/index.html")

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.object.filter(username=username):
        #     messages.error(request, "Username already exists!! Try Other Username!")
        #     return redirect ('home')
        
        # if User.objects.filter(email=email):
        #     messages.error(request, "Email already exists! Please Try Onther Email! ")
        #     return redirect('home')
        
        # if len(username)>10:
        #     messages.error(request, "Username under 10 char!")
        
        # if pass1 != pass2:
        #     messages.error(request, "Passwords not match!!")

        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!")
        #     return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been Successfully Created!, WE have sent you a confirmation email!, Please check It!!")


        # Welcome Email
        # subject = "Welcome to Django Login Home page!!"

        # message = "Hello" + myuser.first_name + "!! \n " + "Welcome to Home Page!! \n Thanks for visiting our website \n we have also sent you a confirmation email, please confirm your email address in order to activate your account. \n \n Thinking You \n Denish"

        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True) 

        return redirect ('signin')


    return render (request, "application/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login (request, user)
            fname = user.first_name
            return render (request, "application/index.html", {'fname' : fname})

        else:
            messages.error(request, "Your Credentials Wrong!")
            return redirect ('home')

    return render (request, "application/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect ('home')
    # return render (request, "application/signout.html")