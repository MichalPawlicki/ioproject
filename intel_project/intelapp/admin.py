from django.contrib import admin
import intelapp.models as models

# Register your models here.


admin.site.register(models.UserGroup)
admin.site.register(models.UserProfile)
admin.site.register(models.FoeGroup)
admin.site.register(models.FoeInfo)