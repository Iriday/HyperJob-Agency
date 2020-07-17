from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy, get_all_vacancies
from django.core.exceptions import PermissionDenied


# Create your views here.

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/vacancies.html", {"vacancies": get_all_vacancies()})


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied

        Vacancy(author=request.user, description=request.POST.get("description")).save()
        return redirect("/home")
