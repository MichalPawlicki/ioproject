from django.db import models

# Create your models here.


class UserGroup(models.Model):
    name = models.CharField(max_length=256, unique=True, blank=False)


class User(models.Model):
    group = models.ForeignKey(UserGroup)
    login = models.CharField(max_length=64, unique=True, blank=False)
    password = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=128, unique=True, blank=False)
    device_id = models.CharField(max_length=16, null=True)
    confirmed = models.BooleanField(default=False, null=False)
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
    submitted_by = models.ForeignKey(User)