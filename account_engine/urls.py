from django.urls import path
from account_engine.views import (HomeView)


urlpatterns = [
path('',HomeView.as_view(), name= 'home')
]
