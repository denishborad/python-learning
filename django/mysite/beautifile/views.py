
from datetime import datetime, timedelta
import secrets
import token
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Register, contactus, Product, LinkGenerate
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdate, ProfileUpdate
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.http import HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site


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
    ch = Register.objects.filter(id=request.user.id)
    if len(ch) > 0:
        data = Register.objects.get(user__id=request.user.id)
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


# error Code

# def password_reset_request(request):
#     if request.method == 'POST':
#         password_form = PasswordResetForm(request.POST)
#         if password_form.is_valid():
#             data = password_form.cleaned_data['email']
#             user_email = User.objects.filter(Q(email=data))
#             if user_email.exists():
#                 for user in user_email:
#                     subject = 'Password Request'
#                     email_template_name = 'password_reset_email.html'
#                     parameters = {
#                         'email': user.email,
#                         'domain': '127.0.0.1:8000',
#                         'site_name': 'BeautiFile',
#                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                         'token': default_token_generator.make_token(user),
#                         'protocol': 'http',
#                     }
#                     email = render_to_string(email_template_name, parameters)

#                     try:
#                         send_mail(subject, email, '', [
#                             user.email], fail_silently=False)

#                     except:
#                         return HttpResponse("Invalid Header")
#                     return redirect('password_reset_done')
#     else:
#         password_form = PasswordResetForm()
#     context = {
#         'password_form': password_form
#     }
#     return render(request, "password_reset_form.html", context)

# error Code


# error Code

# def LinkGenerate(request, uidb64, token):
#     if request.method == 'POST':
#         email = request.POST['email']

#         if not email(email):
#             messages.error(request, 'Email Has Been Not Found!')
#             return render(request, "password_reset_form.html")

#         current_site = get_current_site(request)
#         email_body = {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': account_activation_token.make_token(user),
#         }
#         link = reverse('activate', kwargs={
#             'uidb64': email_body['uid'], 'token': email_body['token']})

#         email_subject = 'Activate your account'

#         activate_url = 'http://'+current_site.domain+link

#         email = EmailMessage(
#             email_subject,
#             'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
#             'noreply@semycolon.com',
#             [email],
#         )

#         email.send(fail_silently=False)
#         return render(request, "password_reset_form.html")

# error Code


def reset_password(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        print(user_email)
        associated_user = User.objects.exclude(
            is_active=0).filter(email=user_email)
        print("email_id")

        token = secrets.token_hex()

        if associated_user.exists():
            id = associated_user.values('id').first()['id']
            user = User.objects.exclude(is_active=0).get(id=id)

            Subject = "Request For Password Reset!"
            text_template = "password_reset_email.txt"
            data = {
                # "email": user_email,
                # "domain": '127.0.0.1:8000',
                # "site_name": 'Website',
                # "user": associated_user,
                # "token": token,
                # "protocol": 'http',
                'email': user_email,
                'domain': '127.0.0.1:8000',
                'site_name': 'BeautiFile',
                'uid': associated_user,
                'token': token,
                'protocol': 'http',
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
    # utoken = token

    # # This is temp timestamp to verify diff of 5 min.
    # temp_timestamp = datetime.now()
    # # temp timestamp converted to unix
    # temp_time = datetime.timestamp(temp_timestamp)*1000
    # convert_temp_timestamp = float(temp_time)  # current time
    # pass_reset_data = LinkGenerate.objects.filter(
    #     token=utoken).values()  # unique token verifies user

    # if pass_reset_data.exists():  # True if user found

    #     email = LinkGenerate.objects.filter(token=utoken).values(
    #         'email').first()['email']  # This is for getting single email id

    #     myuser_id = User.objects.filter(
    #         user_email=email).values_list('user_id')[0][0]

    #     user = User.objects.get(user_id=myuser_id)

    #     # status value for checking link been used or not
    #     status_code = pass_reset_data.values_list('status')[0][0]

    #     exp_time = pass_reset_data.values_list(
    #         'timestamp')[0][0]  # get timestamp from database

    #     convert_unix_timestamp = float(exp_time)
    #     if (convert_unix_timestamp > convert_temp_timestamp) and (status_code == 1):
    #         if request.method == "POST":
    #             pass1 = request.POST['new_pass']
    #             pass2 = request.POST['confirm_pass']

    #             if pass1 == pass2:
    #                 enc_pass = make_password(pass1)
    #                 update_pass = {
    #                     'user_password': enc_pass
    #                 }
    #                 user.update(**update_pass)

    #                 update_status = {
    #                     'status':   0
    #                 }

    #                 pass_reset_data.update(**update_status)

    #             else:
    #                 return redirect('password_reset_confirm')
    return render(request, 'password_reset_confirm.html')


def reset_password_done(request):
    return render(request, 'password_reset_done.html')


def reset_password_complete(request):
    return render(request, 'password_reset_complete.html')
