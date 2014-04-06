import hashlib
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserGroup(models.Model):
    name = models.CharField(max_length=256, unique=True, blank=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(UserGroup)
    device_id = models.CharField(max_length=16, null=True)
    confirmation_code_hash = models.CharField(max_length=128)

    @staticmethod
    def hash_confirmation_code(code):
        return hashlib.sha512(code).hexdigest()


class FoeGroup(models.Model):
    name = models.CharField(max_length=1024, unique=True, blank=False)


class FoeInfo(models.Model):
    YES = 'Y'
    PROBABLY = 'P'
    NO = 'N'
    IS_MILCH_COW_CHOICES = [
        (YES, 'Is a milch cow'),
        (PROBABLY, 'Probably a milch cow'),
        (NO, 'Not a milch cow')
    ]

    foe_group = models.ForeignKey(FoeGroup)
    name = models.CharField(max_length=1024, blank=False)
    comment = models.CharField(max_length=2048)
    level = models.IntegerField()
    defence_strength = models.FloatField()
    is_milch_cow = models.CharField(max_length=1, choices=IS_MILCH_COW_CHOICES,
                                    default=NO)
    submission_time = models.DateTimeField()
    submitted_by = models.ForeignKey(UserProfile)
    published = models.BooleanField(default=False)
