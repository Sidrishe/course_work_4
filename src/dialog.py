from src.HH import HeadHunter
from src.SJ import SuperJobAPI
from src.save_json import SaveVacancy


def user_interaction():

    """Взаимодействие с пользователем"""

    platforms = ['1', '2']

    user_input = input('Введите платформу для поиска: 1 - HeadHunter , 2 - SuperJob \n')

    if user_input == platforms[0]:
        client = HeadHunter()

        search_query = input('Вы выбрали HH \nВведите поисковый запрос: \n')
        hh_vacancy = client.get_vacancies(search_query)
        SaveVacancy().add_vacancy(hh_vacancy)
        print('Сформирован список вакансий \n')

        user_ch = input('Введите ключевое слово: \n')
        SaveVacancy().get_info(user_ch)

        user_pick = input('Хотите отсортировать данных по З/П?: \n')

        if user_pick == 'да' or 'yes':
            SaveVacancy().top_salary_vacancy(hh_vacancy)
        else:
            quit()

    elif user_input == platforms[1]:
        client = SuperJobAPI()
        search_query = input("Вы выбрали SJ \nВведите поисковый запрос: \n")
        sj_vacancy = client.get_vacancies(search_query)
        SaveVacancy().add_vacancy(sj_vacancy)
        print('Сформирован список вакансий \n')

        user_ch = input('Введите ключевое слово: \n')
        SaveVacancy().get_info(user_ch)

        user_pick = input('Хотите отсортировать данных по З/П?: \n')

        if user_pick == 'да' or 'yes':
            SaveVacancy().top_salary_vacancy(sj_vacancy)
        else:
            quit()

    elif user_input not in platforms:
        print('Такой платформы для поиска не предусмотрено')
