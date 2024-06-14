from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Full Name" ,"class":"form-control"}), required = True)    
    username = forms.CharField(widget = forms.TextInput(attrs = { 'class' : 'id form-control', 'placeholder': 'User Name'}), max_length = 100, required = True)
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class" : "id form-control","placeholder": "Phone"}), required = True)
    email = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'id form-control', 'placeholder': 'Email Address'}), required = True)    
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'id form-control', 'placeholder': 'Password'}), required = True)
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'id form-control', 'placeholder': 'Confirm password'}), required = True)



    class Meta:
        model = User
        fields = ['full_name', 'username', 'email','phone','gender','password1', 'password2']