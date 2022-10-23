from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from account_engine.models import Profile
from django.core import serializers

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    def profiles(self):
        profiles = Profile.objects.all()
        return serializers.serialize('geojson',profiles)
