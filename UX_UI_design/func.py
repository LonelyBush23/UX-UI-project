import datetime
import re
import pandas as pd
import requests
from pandas import json_normalize

def check_in(list1, list2):
    for el in list1:
        if el in list2:
            return True
    return False

CLEANR = re.compile('<.*?>')

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def get_vac(page, d):
    prof = ['design', 'ux', 'ui', 'дизайн', 'иллюстратор', 'UX/UI дизайнер']
    time = ['00:00:01', '06:00:00', '12:00:00', '18:00:00', '23:59:59']
    result = []
    for i in range(1, len(time)):
        req_page = requests.get(
            f'https://api.hh.ru/vacancies?specialization=1&per_page=100&page={page}&date_from=2022-12-{d}T{time[i - 1]}&date_to=2022-12-{d}T{time[i]}').json()
        vacancies = req_page['items']
        if len(vacancies) == 0:
            break
        for i in range(len(vacancies)):
            vac_name = vacancies[i]['name']
            if check_in(prof, vac_name):
                name = vacancies[i]['name']
                description = requests.get(f'https://api.hh.ru/vacancies/{vacancies[i]["id"]}').json()['description']
                description = cleanhtml(description)
                key_skills = []
                key_skills_list = requests.get(f'https://api.hh.ru/vacancies/{vacancies[i]["id"]}').json()['key_skills']
                for skills in key_skills_list:
                    key_skills.append(skills.get('name'))
                key_skills = ','.join(key_skills)
                employer_name = vacancies[i]['employer']['name']
                try:
                    salary_currency = vacancies[i]['salary']['currency']
                except:
                    salary_currency = ''
                area_name = vacancies[i]['area']['name']
                published_at = vacancies[i]['published_at'][:10]
                published = published_at.split('-')
                published_at = f'{published[2]}.{published[1]}.{published[0]}'
                result.append({'name': name, 'description': description, 'key_skills': key_skills,
                               'employer_name': employer_name, 'salary_currency': salary_currency,
                               'area_name': area_name, 'published_at': published_at})
                if len(result) == 10:
                    return result
    return result

def get_vacancies(date):
    if len(date) == 1:
        date = '0'+date
    res = []
    for p in range(20):
        v = get_vac(p, date)
        if len(v) == 10:
            res = v
            break
        res = res + v
        if len(res) > 10:
            break
    return res

def is_correct(date):
    try:
        date = int(date)
    except:
        return False
    if (len(str(date)) == 1 and date!=0) or (len(str(date)) == 2 and date>0 and date<=31):
        return True
    else:
        return False
