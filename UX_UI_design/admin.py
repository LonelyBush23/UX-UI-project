from django.contrib import admin
from .models import *


@admin.register(About_profession)
class About_profession_Admin(admin.ModelAdmin):
    list_display = ('header', 'description', 'image')

@admin.register(Relevance)
class About_profession_Admin(admin.ModelAdmin):
    list_display = ('year', 'average_salary', 'average_salary_prof', 'vacancy_count', 'vacancy_count_prof')

@admin.register(Geography_salary)
class About_profession_Admin(admin.ModelAdmin):
    list_display = ('city_salary', 'salary')

@admin.register(Geography_vacancy)
class About_profession_Admin(admin.ModelAdmin):
    list_display = ('city_vacancy', 'vacancy')

@admin.register(Skill)
class About_profession_Admin(admin.ModelAdmin):
    list_display = ('year', 'skills', 'image')

@admin.register(Image)
class About_profession_Admin(admin.ModelAdmin):
    list_display = ('name', 'image')