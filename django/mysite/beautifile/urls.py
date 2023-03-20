from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('client/', views.client, name='client'),
    path('contact/', views.contact, name='contact'),
    path('login1/', views.login1, name='login1'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('contactus/', views.contact_us, name='contactus'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change/', views.change_password, name='change'),
    #     path('password_reset_form/', auth_views.PasswordResetView.as_view(
    #         template_name="password_reset_form.html"), name='password_reset_form'),
    #     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    #          name='password_reset_done'),
    #     path('password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    #          name='password_reset_confirm'),
    #     path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    #          name='password_reset_complete'),
    path("password_reset/", views.reset_password, name='password_reset'),
    path("password_reset/", views.reset_password_done, name='password_reset'),
    path("password_reset_confirm/<uidb64>/<token>/", views.change_forgot_pass,
         name='password_reset_confirm'),
    path("password_reset/", views.reset_password_complete, name='password_reset'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
