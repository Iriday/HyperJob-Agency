from django.shortcuts import render
from django.views import View
from vacancy.models import get_all_vacancies


# Create your views here.
class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/vacancies.html", {"vacancies": get_all_vacancies()})
