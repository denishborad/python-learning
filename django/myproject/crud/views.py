from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import contactus, Users, LinkGenerate, Session
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from datetime import datetime, timedelta
import secrets
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Home(request):
    if 'username' in request.session:
        username = request.session['username']
        customer = Users.objects.filter(username=username).values('userid').first()['userid']
        return render(request,'home.html', {"customer":customer})
    else:
        messages.success(request, "Welcome To The Index Page")

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
            messages.error(request, 'Please chack!! Your Both Password Are Same??')
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
        token = secrets.token_hex() 
        request.session['username'] = username
        request.session['token'] = token
        user = Users.objects.get(username=username)
        user1 = Users.objects.filter(username=user).values('email').first()['email']
        sessions = Session(email=user1, token=token, user=user)
        sessions.save()
        us = authenticate (request, username=username, password=pass1)
        if us is not None:
            login(request, us)
            messages.success(request, "Successfully Login!")
            return redirect('home')
        else:
            messages.error(
                request, "Login Required! Please check your username and password")
            return redirect('login')
    return render(request, 'login.html')

def Logout(request):
    try:
        if 'token' in request.session :
            token = request.session['token']
            print(token)
            customer = Session.objects.filter(token=token).values('session_id').first()['session_id']
            print(customer)
            Session.objects.filter(session_id=customer).update(session_status=1)
            Session.objects.filter(session_id=customer).update(is_deleted=1)
            messages.info(request, "Logged out successfully!")
            return redirect('login')
    except KeyError:
        messages.success(request, "Logged out successfully!")
    return redirect('index')

def Profile(request,userid):
    customers = Users.objects.get(userid=userid)
    return render(request,'profile.html',{'customers':customers})

def profile_update(request,userid):
    custom = Users.objects.get(userid = userid)
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        mobile_no = request.POST['phone']
        if len(request.FILES) != 0 :
            custom.prof_img = request.FILES['img']
        request.session['username']=username
        Users.profileupdate(
            userid=userid,
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=email,
            dob=dob,
            address=address,
            mobile_no=mobile_no,
            prof_img=custom.prof_img
        )

        custom1 = User.objects.filter(email=email).values('id').first()['id'] 
        user = User.objects.get(id=custom1) # For Get Default Id to CustomId
        user.username = username
        user.save()
        print(user,'user')
        # User.objects.filter(username=custom).update(username=username)
        messages.success(request, 'Your profile Updated!')
        return redirect('home')
    else:
        messages.error(request, 'Your Profile not Change!')
        return redirect('profile')

    # if request.method == "POST":
    #     username = request.POST['username']
    #     firstname = request.POST['firstname']
    #     lastname = request.POST['lastname']
    #     email = request.POST['email']
    #     dob = request.POST['dob']
    #     address = request.POST['address']
    #     # prof_img = request.FILES['img']
    #     mobile_no = request.POST['phone']
       
    #     # Update Data
    #     custom = Users.objects.get(userid = userid)
    #     print(custom,'custom')
    #     custom1 = User.objects.filter(username=custom.username).values('id').first()['id'] #For User Id Get and Filter By CustomUsername
    #     user = User.objects.get(id=custom1) # For Get Default Id to CustomId
    #     print(custom1)
    #     user.username = username
    #     user.save()
    #     messages.success(request, 'Your profile Updated!')

    #     custom.username = username
    #     custom.firstname = firstname
    #     custom.lastname = lastname
    #     custom.email = email
    #     custom.dob = dob
    #     custom.address = address
    #     custom.mobile_no = mobile_no
    #     # custom.prof_img = prof_img
    #     custom.save()
    #     messages.success(request, 'Your profile Updated!')

    #     #For User Id Get and Filter By Email

    #     # custom1 = User.objects.filter(email=email).values('id').first()['id'] 
    #     # user = User.objects.get(id=custom1) # For Get Default Id to CustomId
    #     # user.username = username
    #     # user.save()
    #     # print(custom1)
    #     return redirect('home')
    # else:
    #     messages.error(request, 'Your Profile not Change!')
    #     return redirect('home')
    # return render(request,'home.html')

def Lists(request):
    customers = Users.objects.filter(is_delete=0).all()
    paginator = Paginator(customers, 3)
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
    # print(customers)
    contact = {
        'customers':customers
    }
    return render(request,"edit.html", contact)


def UpdateRecord(request, userid):
    if request.method == 'POST':
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
        messages.success(request, 'Your profile Updated!')
        return redirect('lists')
    else:
        messages.error(request, 'Your Profile not Change!')
        return redirect('lists')

# def Delete(request, userid):
#     Users.objects.filter(userid=userid).delete()
#     return redirect("lists")


def Delete(request, userid):
    Users.objects.filter(userid=userid).update(is_delete=1)
    messages.success(request, "User Deleted")
    return redirect('lists')

def ChangePass(request,userid):
    context = {}
    data = Users.objects.get(userid=userid)
    context["data"] = data

    if request.method == "POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        new_pas1 = request.POST["npwd1"]
        if new_pas != new_pas1:
            messages.error(request, "Your New Password Not Same!")
        
        
        user1 = User.objects.get(username=data.username)
         
        check = check_password(current,user1.password)
        
        if check == True:
             
            passw = make_password(new_pas)
            data.pass1=passw
            data.save()
            user1.set_password(passw)    
            user1.save()
            return redirect('home')
        else:
            
            context["msz"] = "Incorrect current password"
            context["col"] = "alert-danger"
        return render(request, 'changepass.html')            
    return render(request, 'changepass.html')


def Product(request):
    return render(request, 'product.html')

def PassReset(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        print(user_email)
        associated_user = Users.objects.exclude(
            is_delete=1).filter(email=user_email)

        token = secrets.token_hex()

        if associated_user.exists():
            id = associated_user.values('userid').first()['userid']
            print(id,'id')
            user = Users.objects.exclude(is_delete=1).get(pk=id)
            print(user,'user')

            Subject = "Request For Password Reset!"
            text_template = "pass_reset_email.txt"
            data = {
                "email": user_email,
                "domain": '127.0.0.1:8000',
                "site_name": 'Website',
                "user": associated_user,
                "token": token,
                "protocol": 'http',
            }

            myemail = render_to_string(text_template, data)

            email = EmailMessage(Subject, myemail, to=[user_email])
            email.send()

            time = datetime.now()+timedelta(days=3)
            expiry = datetime.timestamp(time)*1000

            data1 = LinkGenerate(
                email=user_email,
                status=1,
                token=token,
                expiry=expiry,
            )

            data1.save()
        return redirect('pass_reset_done')
    return render(request, 'pass_reset.html')

def PassResetDone(request):
    return render(request, 'pass_reset_done.html')

def PassResetConfirm(reqeust, token):
    # utoken = request.GET.get('token')
    utoken = token
    print(utoken)

    # This is temp timestamp to verify diff of 5 min.
    temp_timestamp = datetime.now()
    # temp timestamp converted to unix
    temp_time = datetime.timestamp(temp_timestamp)*1000
    convert_temp_timestamp = float(temp_time)  # current time
    pass_reset_data = LinkGenerate.objects.filter(
        token=utoken).values()  # unique token verifies user

    if pass_reset_data.exists():  # True if user found
        email = LinkGenerate.objects.filter(token=utoken).values('email').first()[
            'email']  # This is for getting single email id
        users = User.objects.filter(email=email).values('id').first()['id']

        myuserid = Users.objects.filter(
            email=email).values_list('userid')[0][0]
        print("myuserid", myuserid)

        # status value for checking link been used or not
        status_code = pass_reset_data.values_list('status')[0][0]

        exp_time = pass_reset_data.values_list(
            'expiry')[0][0]  # get timestamp from database
        print("sasfsgasd", status_code, exp_time)
        convert_unix_timestamp = float(exp_time)
        if (convert_unix_timestamp > convert_temp_timestamp) and (status_code == 1):
            if reqeust.method == "POST":
                pass1 = reqeust.POST['new_pass']
                pass2 = reqeust.POST['confirm_pass']

                if pass1 == pass2:
                    enc_pass = make_password(pass1)
                    update_password = {
                        'password': enc_pass,
                    }
                    print("asdsfasf", update_password)
                    User.objects.filter(id=users).update(**update_password)
                    update_pass = {
                        'pass1': enc_pass,
                    }

                    Users.objects.filter(
                        userid=myuserid).update(**update_pass)
                    print('Users',update_pass)

                    update_status = {
                        'status': 0
                    }

                    pass_reset_data.update(**update_status)
                    return redirect('pass_reset_complete')

        else:
            return redirect('pass_reset')
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

def json(request):
    data = list(Users.objects.values())
    print(data)
    return JsonResponse(data, safe=False)