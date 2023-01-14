from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import *
from .func import *


def home_page(request):
    what_is_it = About_profession.objects.get(header='Что такое UX/UI?')
    what_is_it.description = what_is_it.description.split('/n')
    what_do = About_profession.objects.get(header='Чем занимается UX/UI-дизайнер?')
    what_do.description = what_do.description.split('/n')
    what_known = About_profession.objects.get(header='Какие знания и навыки нужны для UX/UI?')
    what_known.description = what_known.description.split('/n')
    ws = About_profession.objects.get(header='Востребованность профессии')
    ws.description = ws.description.split('/n')
    return render(request, 'home.html', {'what_is_it':what_is_it, 'what_do':what_do, 'what_known':what_known, 'ws':ws})


def relevance(request):
    items = Relevance.objects.all().order_by('year').reverse()
    salary = Image.objects.get(name='Уровень зарплат по годам')
    vacancy = Image.objects.get(name='Количество вакансий по годам')
    return render(request, 'relevance.html', {'items': items, 'slary': salary, 'vacancy':vacancy})


def geography(request):
    salary = Geography_salary.objects.all().order_by('salary').reverse()
    vacancy = Geography_vacancy.objects.all().order_by('vacancy').reverse()
    salary_city = Image.objects.get(name='Уровень зарплат по городам')
    vacancy_city = Image.objects.get(name='Доля вакансий по городам')
    return render(request, 'geography.html', {'salary': salary, 'vacancy': vacancy, 'salary_city':salary_city, 'vacancy_city':vacancy_city})


def skills(request):
    skills = Skill.objects.all().order_by('year').reverse()
    return render(request, 'skills.html', {'skills': skills})

def last_vacancies(request):
    if request.method == "GET":
        try:
            date = request.GET['date']
        except:
            date = '777'
    vac = ''
    if is_correct(date):
        try:
            vac = get_vacancies(date)
        except:
            vac = 'Ошибка'
    return render(request, 'vacancies.html', {'vacancies': vac})