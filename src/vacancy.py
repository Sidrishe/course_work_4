class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, title: str, url: str, employer: str, requirements: str, salary_from=0, salary_to=0):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.requirements = requirements

    def __str__(self):
        return f"{self.title} {self.url}"

    def to_dict(self):
        """Формирование удобного для чтения файла"""
        return {
            'Профессия': self.title,
            'Ссылка': self.url,
            'З/п от': self.salary_from,
            'З/п до': self.salary_to,
            'Работодатель': self.employer,
            'Требования': self.requirements

        }

    def __ge__(self, other):
        return self.salary_to >= other.salary_to

    def __le__(self, other):
        return self.salary_to >= other.salary_to

    def __eq__(self, other):
        return self.salary_to == other.salary_to
