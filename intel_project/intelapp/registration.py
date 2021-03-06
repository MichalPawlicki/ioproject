import hashlib
from intelapp.models import UserProfile, UserGroup

__author__ = 'michal'
from django.core.mail import send_mail
from django.db import transaction
from intelapp import utils
from django.contrib.auth.models import User


class RegistrationManager(object):
    @staticmethod
    def activate_user(confirmation_code):
        code_hash = UserProfile.hash_confirmation_code(confirmation_code)
        try:
            user_profile = UserProfile.objects.get(
                confirmation_code_hash=code_hash)
            return RegistrationManager._activate_profile(user_profile)
        except UserProfile.DoesNotExist:
            return None

    @staticmethod
    def _activate_profile(user_profile):
        try:
            with transaction.atomic():
                user_profile.confirmation_code_hash = ''
                user_profile.save()
                user = user_profile.user
                user.is_active = True
                user.save()
                return user
        except Exception:
            return None

    @staticmethod
    def send_activation_email(email, username, confirmation_code):
        subject = 'Intelapp - activate account'
        content = 'Hi, {0}! Visit the following URL to activate your account: '.format(
            username) + \
            '<server_name>/intel/register/confirm/{0}'.format(
            confirmation_code)
        send_mail(subject,
                  content,
                  'intelprojectclient@gmail.com',
                  [email],
                  fail_silently=False)

    @staticmethod
    def create_inactive_user(username, email, password, group, device_id):
        confirmation_code = utils.random_string(128)
        hashed_code = hashlib.sha512(confirmation_code).hexdigest()
        try:
            with transaction.atomic():
                new_user = User.objects.create_user(username, email, password)
                new_user.is_active = False
                new_user.save()
                new_group, _ = UserGroup.objects.get_or_create(name=group)
                UserProfile.objects.create(user=new_user, group=new_group,
                                           device_id=device_id,
                                           confirmation_code_hash=hashed_code)
                RegistrationManager.send_activation_email(email, username,
                                                          confirmation_code)
                return new_user
        except Exception:
            return None
