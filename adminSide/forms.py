from django import forms
from .models import *
# from .models import Products, ProductInfo


# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Register
#         fields = ['username', 'password', 'email']
#         labels = {'username': "Enter name", 'password': "Enter Password", 'email': "Enter Email"}
#         error_messages = {'username':{'required': "username field can not be empty"}, 'password':{'required': "password field can not be empty"}, 'email':{'required': "email field can not be empty"}}
#         widgets = {'password': forms.PasswordInput(attrs={'placeholder':'password', 'class': "form-control"}), 'username': forms.TextInput(attrs={'placeholder':'username', 'class': "form-control"}), 'email': forms.TextInput(attrs={'placeholder':'email', 'class': "form-control"})}



# class ProductsForm(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = ['name', 'disc', 'img']
        # widgets = {'name': forms.TextInput(attrs={ 'class': "form-control"}), 'disc': forms.TextInput(attrs={ 'class': "form-control"}), 'img': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) }


# class ProductsinfoForm(forms.ModelForm):
#     class Meta:
#         model = ProductInfo
#         fields = '_all_'