from django.contrib.auth.models import User
from .models import UserDetails
from django import forms


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['mobile_no', 'profile_pic', 'dob']
