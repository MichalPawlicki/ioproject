from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

__author__ = 'michal'


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(widget=PasswordInput())
    email = forms.EmailField()
    group = forms.CharField()
    device_id = forms.CharField(required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError(
                'User with provided username already exists.')
        return username

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirmed_password = cleaned_data.get('confirm_password')
        if password != confirmed_password:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data