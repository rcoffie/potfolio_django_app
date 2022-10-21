from django.contrib import admin
from account_engine.models import CustomUser, Profile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Profile)