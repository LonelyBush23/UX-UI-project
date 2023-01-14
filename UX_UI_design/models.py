from django.db import models
import django_tables2 as tables



class About_profession(models.Model):
    header = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='static/djangoProject/img',blank=True)

    def __str__(self):
        return self.header


class Relevance(models.Model):
    year = models.IntegerField()
    average_salary = models.IntegerField()
    average_salary_prof = models.IntegerField()
    vacancy_count = models.IntegerField()
    vacancy_count_prof = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Geography_salary(models.Model):
    city_salary = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.city_salary

class Geography_vacancy(models.Model):
    city_vacancy = models.CharField(max_length=100)
    vacancy = models.FloatField()

    def __str__(self):
        return self.city_vacancy

class Skill(models.Model):
    year = models.IntegerField()
    skills = models.TextField()
    image = models.ImageField(upload_to='static/djangoProject/img', blank=True)

    def __str__(self):
        return str(self.year)

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/djangoProject/img')

    def __str__(self):
        return self.name
