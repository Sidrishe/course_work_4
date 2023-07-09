import json
import requests
from src.vacancy import Vacancy
from src.AbstractClass import AbstractAPIVacancy


class HeadHunter(AbstractAPIVacancy):

    def __init__(self):
        pass

    def get_vacancies(self, job_title):
        """Запрос к API HH"""

        params = {
            'text': job_title,
            'per_page': 50
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        js_obj = json.loads(data)
        return self.vacancies_pars(js_obj)

    def vacancies_pars(self, js_obj):
        """Парсинг полученных вакансий"""

        all_vacancy = []
        for obj in js_obj['items']:
            salary = obj.get('salary') or {}
            all_vacancy.append(Vacancy(**{
                'title': obj['name'],
                'salary_from': salary.get('from', 0),
                'salary_to': salary.get('to', 0),
                'employer': obj['employer']['name'],
                'url': obj['url'],
                'requirements': obj['snippet']['requirement']
            }))

        return all_vacancy
