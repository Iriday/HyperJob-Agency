from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume, get_all_resumes
from django.core.exceptions import PermissionDenied


# Create your views here.

class ResumesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "resume/resumes.html", {"resumes": get_all_resumes()})


class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_staff:
            raise PermissionDenied

        Resume(author=request.user, description=request.POST.get("description")).save()
        return redirect("/home")
