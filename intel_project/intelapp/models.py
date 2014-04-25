import hashlib
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FoeGroup(models.Model):
    name = models.CharField(max_length=1024, unique=True, blank=False)
    
    def __unicode__(self):
        return self.name
    
class UserGroup(models.Model):
    name = models.CharField(max_length=256, unique=True, blank=False)
    current_foe = models.ForeignKey(FoeGroup,null=True)
    battle_ending = models.DateTimeField(null=True)
    #Null=True, in case a group doesn't have a leader
    # 'string trick'
    leader = models.ForeignKey('UserProfile',null=True)
    def __unicode__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(UserGroup)
    device_id = models.CharField(max_length=16, null=True)
    confirmation_code_hash = models.CharField(max_length=128)
    is_officer = models.BooleanField(default=True)
    @staticmethod
    def hash_confirmation_code(code):
        return hashlib.sha512(code).hexdigest()
    
    def __unicode__(self):
        return self.user.username
    


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
    submission_time = models.DateTimeField(default=datetime.datetime.now())
    submitted_by = models.ForeignKey(UserProfile)
    
    def __unicode__(self, ):
        return self.name
    
    published = models.BooleanField(default=False)

    @staticmethod
    def get_newest_visible_info(foe_name, user):
        matching_info = FoeInfo.objects.filter(name=foe_name)
        if not matching_info:
            return None
        retriever_profile = user.get_profile()
        retriever_group = retriever_profile.group
        is_info_visible_predicate = lambda info:\
            info.published or info.submitted_by.group == retriever_group
        visible_info = filter(is_info_visible_predicate, matching_info)
        if not visible_info:
            return None
        return sorted(visible_info, key=lambda info: info.submission_time,
                      reverse=True)[0]