
from datetime import datetime, timedelta
import secrets
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from .models import Register, contactus, Product, LinkGenerate
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdate, ProfileUpdate
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password


# Create your views here.


def index(request):
    allpro = Product.objects.all()
    # print(allpro)
    # for item in allpro:
    #     print(item.pTitle)
    context = {'ind': allpro}
    return render(request, 'index.html', context)


def product(request):
    allpro = Product.objects.all()
    # print(allpro)
    # for item in allpro:
    #     print(item.pTitle)
    context = {'ind': allpro}
    return render(request, 'product.html', context)


def about(request):
    return render(request, 'about.html')


def client(request):
    return render(request, 'client.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        Email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        img = request.FILES['img']
        # if User.object.filter(username=username):
        #     messages.error(
        #         request, "Username already exists!! Try Other Username!")
        #     return redirect('register')

        # if User.objects.filter(email=Email):
        #     messages.error(
        #         request, "Email already exists! Please Try Onther Email! ")
        #     return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords not match!!")
            return redirect('register')
        my_user = Register(uname=username,
                           email=Email, password=password1, profile_image=img)
        my_user.save()

        myuser = User.objects.create_user(username, Email, password1)
        myuser.save()

        messages.success(request, "successfully Register!!")

        return redirect('index')
    # print(username, Email, password1, password2)
    return render(request, 'login1.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            # request.session['user_id'] = user.id
            login(request, user)
            context = {'asd': username}
            messages.success(request, "Successfully Login!")
            return render(request, 'index.html', context)
        else:
            messages.error(
                request, "Login Required! Please check your username and password")
            return redirect('index')
    return render(request, 'login1.html')


def Logout(request):
    logout(request)
    try:
        del request.session['user_id']
        messages.info(request, "Your Session ID has been deleted!")
        return redirect('index')
    except KeyError:
        messages.success(request, "Logged out successfully!")
    return redirect('index')


def contact_us(request):
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


def login1(request):
    return render(request, 'login1.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES,
                               instance=request.user.userdetails)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.info(request, "Your Profile Updated!")
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.userdetails)
    return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form})


def change_password(request):
    context = {}
    ch = Register.objects.filter(user_id=request.user.id)
    if len(ch) > 0:
        data = Register.objects.get(user_id=request.user.id)
        context["data"] = data

    if request.method == "POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]

        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)

        if check == True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request, user)
        else:
            context["msz"] = "Incorrect current password"
            context["col"] = "alert-danger"

    return render(request, 'change.html', context)


# True Code

# def send_forgot_password_mail(email, token):
#     subject = "Your forgot password link"
#     text_template = "password_reset_email.html"
#     # EMAIL FORMAT
#     data = {
#         'domain':   '127.0.0.1:8000',
#         'site_name':   'Website',  # Data which will send with E-mail id
#         'token':   token,
#         'protocol':   'http',
#     }

#     myemail = render_to_string(text_template, data)
#     recipient_list = [email]
#     # Formats Email message
#     email = EmailMessage(subject, myemail, to=recipient_list)
#     email.send()
#     return True

# True Code

def reset_password(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        print(user_email)
        associated_user = User.objects.exclude(
            is_active=0).filter(email=user_email)

        token = secrets.token_hex()

        if associated_user.exists():
            id = associated_user.values('pk').first()['pk']
            user = User.objects.exclude(is_active=0).get(pk=id)

            Subject = "Request For Password Reset!"
            text_template = "password_reset_email.txt"
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
    return render(request, 'password_reset.html')


def change_forgot_pass(request, token):

    # utoken = request.GET.get('token')
    utoken = token
    print(utoken)

    # uid = User.objects.get(id=user_id)
    # text = LinkGenerate.objects.filter(user_id=data)
    # print("asfsdgsagsarhrhstz", uid)

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

        myuser_id = Register.objects.filter(
            email=email).values_list('user_id')[0][0]
        print("myuser_id", myuser_id)

        # text = Register.objects.filter(user_id=myuser_id)
        # print(text)
        # user = User.objects.get(id=users)
        # print(user)

        # status value for checking link been used or not
        status_code = pass_reset_data.values_list('status')[0][0]

        exp_time = pass_reset_data.values_list(
            'expiry')[0][0]  # get timestamp from database
        print("sasfsgasd", status_code, exp_time)
        convert_unix_timestamp = float(exp_time)
        if (convert_unix_timestamp > convert_temp_timestamp) and (status_code == 1):
            if request.method == "POST":
                pass1 = request.POST['new_pass']
                pass2 = request.POST['confirm_pass']

                if pass1 == pass2:
                    enc_pass = make_password(pass1)
                    update_pass = {
                        'password': enc_pass
                    }
                    print("asdsfasf", update_pass)

                    Register.objects.filter(
                        user_id=myuser_id).update(**update_pass)
                    User.objects.filter(id=users).update(**update_pass)

                    # update_status = {
                    #     'status': 0
                    # }

                    # pass_reset_data.update(**update_status)
        else:
            return redirect('password_reset')
    return render(request, 'password_reset_confirm.html')


def reset_password_complete(request):
    return render(request, 'password_reset_complete.html')
