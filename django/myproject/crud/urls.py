from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',views.Index, name='index'),
    path('', views.Home, name='home'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/<int:userid>', views.Profile, name='profile'),
    path('profile/profileupdate/<int:userid>', views.profile_update, name='profileupdate'),
    path('lists/', views.Lists, name='lists'),
    path('edit/<int:userid>', views.Edits, name='edit'),
    path('edit/updaterecord/<int:userid>', views.UpdateRecord, name='updaterecord'),
    path('delete/<int:userid>',views.Delete,name='delete'),
    path('changepass/<int:userid>',views.ChangePass,name='changepass'),
    path('product/', views.Product, name='product'),
    path('pass-reset/', views.PassReset, name='pass_reset'),
    path('pass-reset-done/', views.PassResetDone, name='pass_reset_done'),
    path('pass-reset-confirm/<slug:token>/', views.PassResetConfirm, name='pass_reset_confirm'),
    path('pass-reset-complete/', views.PassResetComplete, name='pass_reset_complete'),
    path('contact-us/', views.ContactUs, name='contact'),
    path('about/', views.About, name='about'),
    path('json/',views.json, name='json'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)