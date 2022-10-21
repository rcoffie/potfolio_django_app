from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from account_engine.models import CustomUser, Profile

# Register your models here.

class ProfileAdmin(LeafletGeoAdmin):
    list_display = ('user', 'location')

admin.site.register(CustomUser)
admin.site.register(Profile, ProfileAdmin)