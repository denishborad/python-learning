from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import contactus, Users
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

def Home(request):
    use = request.session['username']
    print(use,'Hello1')
    # username = request.session['username']
    # print(username)
    customer = Users.objects.filter(username=use).values('userid').first()['userid']
    print(customer)
    
    return render(request,'home.html', {"customer":customer})

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
            
            signup = Users(username=username,firstname=firstname,lastname=lastname,email=email,pass1=pass1,prof_img=prof_img)
            signup.save()

            messages.success(request, 'Sign Up Successfully!!')
            return redirect('login')
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        request.session['username'] = username
        print(username,'Hello')
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

def Profile(request,userid):
    customers = Users.objects.get(userid=userid)
    print("user id of cust",customers.userid)
    return render(request,'profile.html',{'customers':customers})

def profile_update(request,userid):
    print("user id",userid,type(userid))
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        # prof_img = request.FILES['img']
        mobile_no = request.POST['phone']
       
        # Update Data
        custom = Users.objects.get(userid = userid)
        custom1 = User.objects.filter(username=custom.username).values('id').first()['id'] #For User Id Get and Filter By CustomUsername
        user = User.objects.get(id=custom1) # For Get Default Id to CustomId
        user.username = username
        user.save()
        print(custom1)
        print(custom)

        custom.username = username
        custom.firstname = firstname
        custom.lastname = lastname
        custom.email = email
        custom.dob = dob
        custom.address = address
        custom.mobile_no = mobile_no
        # custom.prof_img = prof_img
        custom.save()

        #For User Id Get and Filter By Email

        # custom1 = User.objects.filter(email=email).values('id').first()['id'] 
        # user = User.objects.get(id=custom1) # For Get Default Id to CustomId
        # user.username = username
        # user.save()
        # print(custom1)
        return redirect('home')
    # return render(request,'home.html')

def Lists(request):
    customers = Users.objects.filter(is_delete=0).all()
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
    customers = Users.objects.get(userid = userid)
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
    prof_img = request.FILES['img']
    empl = Users.objects.get(userid = userid)
    empl.username = username
    empl.firstname = firstname
    empl.lastname = lastname
    empl.email = email
    empl.prof_img = prof_img
    empl.save()
    # empl = Users.objects.filter(userid=userid).update(is_delete=0)
    return redirect('lists')

# def delete(request, emp_id):
#     Employee.objects.filter(emp_id=emp_id).delete()
#     return render(request,"create.html")


def Delete(request, userid):
    Users.objects.filter(userid=userid).update(is_delete=1)
    return redirect('lists')

def ChangePass(request):
    # user = Users.objects.get(userid=userid)
    # print(user)
    # context = {}
    # ch = Users.objects.filter(userid=request.user.id)
    # if len(ch) > 0:
    #     data = Register.objects.get(user_id=request.user.id)
    #     context["data"] = data

    # if request.method == "POST":
    #     current = request.POST["cpwd"]
    #     new_pas = request.POST["npwd"]

    #     user = User.objects.get(id=request.user.id)
    #     un = user.username
    #     check = user.check_password(current)

    #     if check == True:
    #         user.set_password(new_pas)
    #         user.save()
    #         context["msz"] = "Password Changed"
    #         context["col"] = "alert-success"
    #         user = User.objects.get(username=un)
    #         login(request, user)
    #     else:
    #         context["msz"] = "Incorrect current password"
    #         context["col"] = "alert-danger"

    return render(request, 'changepass.html')


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