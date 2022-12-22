from django.contrib import admin
from django.urls import path, include
from accounts.views import login_page

urlpatterns = [
    path('login/', login_page, name="login"),
]