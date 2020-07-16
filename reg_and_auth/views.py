from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import AuthenticationForm, LoginView


# Create your views here.
class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "reg_and_auth/signup.html"


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = "reg_and_auth/login.html"
