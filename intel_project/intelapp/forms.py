from django import forms
from django.forms.widgets import PasswordInput

__author__ = 'michal'


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(widget=PasswordInput())
    email = forms.EmailField()
    group = forms.CharField()
    device_id = forms.CharField(required=False)