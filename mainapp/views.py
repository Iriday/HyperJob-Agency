from django.shortcuts import render
from django.views import View
from django.core.exceptions import PermissionDenied


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="mainapp/main_page.html")


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied

        return render(request, template_name=("vacancy/new_vacancy.html" if request.user.is_staff
                                              else "resume/new_resume.html"))
