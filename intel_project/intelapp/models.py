from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserGroup(models.Model):
    name = models.CharField(max_length=256, unique=True, blank=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(UserGroup)
    device_id = models.CharField(max_length=16, null=True)
    confirmation_code = models.CharField(max_length=128)


class FoeGroup(models.Model):
    name = models.CharField(max_length=1024, unique=True, blank=False)


class FoeInfo(models.Model):
    foe_group = models.ForeignKey(FoeGroup)
    name = models.CharField(max_length=1024, blank=False)
    comment = models.CharField(max_length=2048)
    level = models.IntegerField()
    strength = models.FloatField()
    submission_time = models.DateTimeField()
    submitted_by = models.ForeignKey(UserProfile)