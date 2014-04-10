from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from intelapp.models import FoeInfo

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


class SubmitFoeInfoForm(forms.Form):
    group = forms.CharField(max_length=1024)
    name = forms.CharField(max_length=1024)
    comment = forms.CharField(max_length=2048)
    level = forms.IntegerField()
    defence_strength = forms.RegexField(regex=r'\d{1,3}([,.]\d{1,3})?[kKmM]?')
    is_milch_cow = forms.ChoiceField(choices=[
        ('Y', 'yes'),
        ('P', 'probably'),
        ('N', 'no')
    ])

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SubmitFoeInfoForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(SubmitFoeInfoForm, self).clean()
        name = cleaned_data.get('name')
        level = cleaned_data.get('level')
        current_user = self.request.user
        newest_visible_info = FoeInfo.get_newest_visible_info(name,
                                                              current_user)
        if newest_visible_info and newest_visible_info.level > level:
            raise forms.ValidationError(
                'A piece of info about this foe with a higher level already '
                'exists in the database.')
        return cleaned_data
