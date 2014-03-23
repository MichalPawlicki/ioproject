from django.contrib import admin
import gameintelligence.models as models

# Register your models here.


admin.site.register(models.UserGroup)
admin.site.register(models.User)
admin.site.register(models.FoeGroup)
admin.site.register(models.FoeInfo)