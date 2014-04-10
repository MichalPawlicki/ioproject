import hashlib
import random
import string
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render

from django.template import RequestContext, loader

# Create your views here.
from django.views.decorators.http import require_GET
from django.views.generic import FormView

#For main site, it will need to be a ListView to list current opponents
from django.views.generic import ListView
from intelapp.models import FoeInfo,FoeGroup
###
from intelapp import utils
from intelapp.forms import RegisterForm
from intelapp.models import UserProfile, UserGroup, RegistrationManager


def index(request):
    return HttpResponse("Hello!")


def index_with_number(request, number):
    return HttpResponse(str(number))


class RegisterView(FormView):
    template_name = 'intelapp/register.html'
    form_class = RegisterForm
    success_url = '/intel/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        group = form.cleaned_data['group']
        device_id = form.cleaned_data['device_id']
        RegistrationManager.create_inactive_user(username, email, password, group, device_id)
        return super(RegisterView, self).form_valid(form)


def confirm_registration(request, code):
    activated_user = RegistrationManager.activate_user(code)
    if not activated_user:
        return HttpResponse('Error when activating user.')
    username = activated_user.username
    return HttpResponse('User "{0}" activated!'.format(username))


def main(request):
    context={}
    return render(request,'intelapp/main.html',context)

    
