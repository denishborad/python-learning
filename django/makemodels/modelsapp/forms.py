from django import forms

class InputForm(forms.Form):
    First_Name = forms.CharField(max_length=200)
    Last_Name = forms.CharField(max_length=200)
    Roll_No = forms.IntegerField(help_text="Enter 6 digit roll number")
    Password = forms.CharField(widget=forms.PasswordInput())