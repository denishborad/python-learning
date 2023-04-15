from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import SignUp, UserProfile, contactus
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

def Home(request):
    return render(request,'home.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        prof_img = request.FILES['img']
        if pass1 != pass2:
            messages.error(request, 'please!! Your Both Password Are Same??')
            return redirect('signup')
        else:
            sign = User.objects.create_user(username,email,pass1)
            sign.save()
            
            signup = SignUp(username=username,firstname=firstname,lastname=lastname,email=email,pass1=pass1,prof_img=prof_img)
            signup.save()

            messages.success(request, 'Sign Up Successfully!!')
            return redirect('login')
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        us = authenticate (request, username=username, password=pass1)
        print(us)
        if us is not None:
            login(request, us)
            messages.success(request, "Successfully Login!")
            return redirect('home')
        else:
            messages.error(
                request, "Login Required! Please check your username and password")
            return redirect('home')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    try:
        del request.session['userid']
        messages.info(request, "Your Session ID has been deleted!")
        return redirect('home')
    except KeyError:
        messages.success(request, "Logged out successfully!")
    return redirect('home')

# def Profile(request, userid):
#     customers = SignUp.objects.get(userid = userid)
#     print(customers)
#     contact = {
#         'customers':customers
#     }
#     return render(request,'profile.html',contact)

# def profile_update(request):
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         user_profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
#     else:
#         user_form = UserUpdateForm(instance=request.user)
#         user_profile = ProfileUpdateForm(instance=request.user)
#     context={
#         'user_form':user_form,
#         'user_profile':user_profile,
#     }
#     return render(request, 'profileupdate.html', context)

def Profile(request,userid):
    customers = SignUp.objects.get(userid = userid)
    # print(customers)
    contact = {
        'customers':customers
    }
    return render(request,'profile.html', contact)

def profile_update(request,userid):
   print("user id",userid,type(userid))
   if request.method == "POST":

        username = request.POST['username']
   
        firstname = request.POST['firstname']

        lastname = request.POST['lastname']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        prof_img = request.FILES['img']
        mobile_no = request.POST['phone']


        # custom = UserProfile.objects.get(userprof = userid)
        custom = SignUp.objects.get(userid=userid)
        # print(custom)
        custom.username = username
        custom.firstname = firstname
        custom.lastname = lastname
        custom.email = email
        custom.dob = dob
        custom.address = address
        custom.mobile_no = mobile_no
        custom.prof_img = prof_img
        custom.save()


        # custom = SignUp.objects.filter(userprof=userid).update(is_delete=1)
        return redirect('home')

def Lists(request):
    customers = SignUp.objects.filter(is_delete=0).all()
    paginator = Paginator(customers, 1)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)
    lastpage = customers.paginator.num_pages

    context = {
        'customers': customers,
        'lastpage': lastpage,
        'pagelist': [n+1 for n in range(lastpage)]
    }

    return render(request, 'lists.html', context)

def Edits(request, userid):
    customers = SignUp.objects.get(userid = userid)
    print(customers)
    contact = {
        'customers':customers
    }
    return render(request,"edit.html", contact)


def UpdateRecord(request, userid):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    prof_img = request.POST['img']
    empl = SignUp.objects.get(userid = userid)
    empl.username = username
    empl.firstname = firstname
    empl.lastname = lastname
    empl.email = email
    empl.prof_img = prof_img
    empl.save()
    empl = SignUp.objects.filter(userid=userid).update(is_delete=0)
    return redirect('lists')

# def delete(request, emp_id):
#     Employee.objects.filter(emp_id=emp_id).delete()
#     return render(request,"create.html")


def Delete(request, userid):
    SignUp.objects.filter(userid=userid).update(is_delete=1)
    return redirect('lists')

def Product(request):
    return render(request, 'product.html')

def PassReset(request):
    return render(request, 'pass_reset.html')

def PassResetDone(request):
    return render(request, 'pass_reset_done.html')

def PassResetConfirm(reqeust):
    return render(reqeust, 'pass_reset_confirm.html')

def PassResetComplete(request):
    return render(request, 'pass_reset_complete.html')

def ContactUs(request):
    if request.method == "POST":
        Subject = request.POST["Subject"]
        Yourname = request.POST["Yourname"]
        Yourmail = request.POST["Yourmail"]
        Message = request.POST["Message"]
        Contactus = contactus(Subject=Subject, Yourname=Yourname,
                              Yourmail=Yourmail, Message=Message)
        Contactus.save()
        messages.info(request, "Thanks for Your Replay!")
    return render(request, 'contactus.html')
    return render(request, 'contactus.html')

def About(request):
    return render(request, 'about.html')