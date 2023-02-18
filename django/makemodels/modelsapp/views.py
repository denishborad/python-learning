from django import forms
from django.shortcuts import render,HttpResponse,redirect
from modelsapp.models import Model1,Model2,Model3,ContactUs
from django.contrib.auth import authenticate,login
from .forms import InputForm

# Create your views here.
def Home(request):
    return render(request,'home.html')

def Model_1(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            return HttpResponse('please enter right password!')
        else:
            mm = Model1(firstname=fname,secondname=sname,Email=email,phone=phone,pass1=pass1)
            mm.save()
            return redirect('model2')

    return render(request,'model1.html')

def Model_2(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        pass1 = request.POST['pass']
        aa = Model2(firstname=firstname,pass1=pass1)
        aa.save()
        mm = authenticate(request, fname=firstname, password=pass1)
        print("Hello", mm)
        if mm is None:
            login(request, mm)
            return redirect('home')
        else:
            return HttpResponse('Login Required!')

    return render(request,'model2.html')

def Model_3(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        m = Model3(name=name,email=email,desc=desc)
        m.save()
        return redirect('contactus')
        print(name,email,desc)
    return render(request,'model3.html')

def Contact_us(request):
    if request.method == 'POST':
        yourname = request.POST['name']
        youremail = request.POST['email']
        subject =request.POST['subject']
        message = request.POST['message']

        m = ContactUs(yourname=yourname, youremail=youremail, subject=subject, yourmessage=message)
        m.save()
        return redirect('home')
        print(yourname, youremail, subject, message)
    return render(request,'contactus.html')


def index_view(request):
    return render(request, 'index.html', {'form': forms})