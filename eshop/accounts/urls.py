from django.contrib import admin
from django.urls import path, include
from accounts.views import login_page, register_page  , activate_email

urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('register/<email_token>/', activate_email, name="activate_email"),

]