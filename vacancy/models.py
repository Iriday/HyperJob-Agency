from django.db import models
from django.db.models import CharField, ForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Vacancy(models.Model):
    description = CharField(max_length=1024)
    author = ForeignKey(User, on_delete=models.CASCADE)


def get_all_vacancies():
    return Vacancy.objects.all()
