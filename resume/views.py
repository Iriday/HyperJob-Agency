from django.shortcuts import render
from django.views import View
from resume.models import get_all_resumes


# Create your views here.

class ResumesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "resume/resumes.html", {"resumes": get_all_resumes()})
