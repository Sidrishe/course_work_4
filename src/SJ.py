import requests
import os
from src.vacancy import Vacancy
from src.AbstractClass import AbstractAPIVacancy


class SuperJobAPI(AbstractAPIVacancy):

    def __init__(self):
        pass

    def get_vacancies(self, job_title):

        """Запрос к API SJ"""

        params = {
                'count': 50,
                'keyword': job_title
                  }

        api_key: str = os.getenv("YT_API_KEY")
        headers = {'X-Api-App-Id': api_key}
        req = requests.get('https://api.superjob.ru/2.0/%s' % 'vacancies/', params, headers=headers)
        return self.vacancies_pars(req.json())

    def vacancies_pars(self, js_obj):

        """Парсинг полученных вакансий"""

        all_vacancy = []
        for obj in js_obj['objects']:
            all_vacancy.append(Vacancy(**{
                'title': obj['profession'],
                'salary_from': obj['payment_from'],
                'salary_to': obj['payment_to'],
                'employer': obj['firm_name'],
                'url': obj['link'],
                'requirements': obj['candidat']
            }))
        return all_vacancy
