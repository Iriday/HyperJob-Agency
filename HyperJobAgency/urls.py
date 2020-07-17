"""HyperJobAgency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import MainPageView, ProfileView
from resume.views import ResumesView, NewResumeView
from vacancy.views import VacanciesView
from reg_and_auth.views import MySignupView, MyLoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view()),
    path("home/", ProfileView.as_view()),
    path("resumes/", ResumesView.as_view()),
    path("resume/new", NewResumeView.as_view()),
    path("vacancies/", VacanciesView.as_view()),

    path("signup", MySignupView.as_view()),
    path("signup/", RedirectView.as_view(url="/signup")),
    path("login", MyLoginView.as_view()),
    path("login/", RedirectView.as_view(url="/login")),
    path("logout/", LogoutView.as_view())
]
