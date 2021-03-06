
import random

# соответствие месяца и его названия
months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта'
}

# соответствие дня и его названия
days = {
    '05': 'пятое',
    '08': 'восьмое',
    '09': 'девятое',
    '13': 'тринадцатое',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '31': 'тридцать первое'
}

# словарь известных людей и из дат рождения
FAMOUS = {'Чехов': '29.01.1860', 'Высоцкий': '25.01.1938', 'Менделеев': '08.02.1834',
          'Крылов': '13.02.1769', 'Ушаков': '24.02.1744', 'Гагарин': '09.03.1934',
          'Чуковский': '31.03.1882', 'Смоктуновский': '28.03.1925', 'Шаляпин': '13.02.1873',
          'Матросов': '05.02.1924'
}


def date_to_str(date):
    """
    Функция приводит дату к текстовому виду
    :param date: дата в формате dd.mm.yyyy
    :return: дата в текстовом виде
    """
    day, month, year = date.split('.')
    result = f'{days[day]} {months[month]} {year} года'
    return result


def run_victory():
    """
    Функция запуска игры викторина
    :return:
    """
    is_play = True
    while is_play:
        # брем 2х из 3х известных людей (только их имена)
        random_famous = random.sample(list(FAMOUS.keys()), 5)
        # идем по именам
        for item in random_famous:
            # просим ввести дату рождения
            answer = input(f'Дата рождения {item} в формате dd.mm.yyyy ')
            # получаем правильный ответ
            true_answer = FAMOUS[item]
            # сравниваем
            if answer == true_answer:
                print('Верно')
            else:
                print('Неверно')
                # получаем дату в текстовом виде
                correct_answer = date_to_str(true_answer)
                # выводим
                print(f'Правильный ответ: {correct_answer}')

        play_again = None
        # Будем спрашивать пока не ответят Да или Нет
        while play_again not in ('Да', 'Нет'):
            play_again = input('Хотите поиграть еще (Да/Нет)? ')

        # Да - продолжаем, Нет - выходим
        is_play = play_again == 'Да'


# def get_date(date):
#     day_list = ['первое', 'второе', 'третье', 'четвёртое',
#                 'пятое', 'шестое', 'седьмое', 'восьмое',
#                 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
#                 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
#                 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
#                 'двадцать первое', 'двадцать второе', 'двадцать третье',
#                 'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
#                 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
#                 'тридцатое', 'тридцать первое']
#     month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
#                   'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
#     date_list = date.split('.')
#     return (day_list[int(date_list[0]) - 1] + ' ' +
#             month_list[int(date_list[1]) - 1] + ' ' +
#             date_list[2] + ' года')


# def victory():
#     famous_people = {'Чехов': '29.01.1860', 'Высоцкий': '25.01.1938', 'Менделеев': '08.02.1834',
#                      'Крылов': '13.02.1769', 'Ушаков': '24.02.1744', 'Гагарин': '09.03.1934',
#                      'Чуковский': '31.03.1882', 'Смоктуновский': '28.03.1925', 'Шаляпин': '13.02.1873',
#                      'Матросов': '05.02.1924'
#                      }
#     import random
#
#     result = random.sample(famous_people.keys(), 5)
#     print(type(result))
#     print(result)
#     # for i in range(5)
#     answer_1 = input('Введите ДР ' + result[0] + ' дд.мм.гггг: ')
#     answer_2 = input('Введите ДР ' + result[1] + ' дд.мм.гггг: ')
#     answer_3 = input('Введите ДР ' + result[2] + ' дд.мм.гггг: ')
#     answer_4 = input('Введите ДР ' + result[3] + ' дд.мм.гггг: ')
#     answer_5 = input('Введите ДР ' + result[4] + ' дд.мм.гггг: ')
#     variant = {result[0]: answer_1, result[1]: answer_2, result[2]: answer_3, result[3]: answer_4, result[4]: answer_5}
#     cnt_true_answer = 0
#     for i in variant.items():
#         print(f'{i[0]} Ваш ответ: {i[1]}')
#         if i[1] == famous_people[i[0]]:
#             cnt_true_answer += 1
#             print('   Правильно!')
#         else:
#             print(f'   Неправильно! (Правильный ответ!: {get_date(famous_people[i[0]])})')
#     print('*************')
#     print(f'Вы угадали {cnt_true_answer} ДР')


# def my_bank_score():
#     score_sum = 0
#     history = []
#
#
#     def buy(score_sum):
#         cost = int(input('Введите сумму покупки: '))
#         if cost > score_sum:
#             print('На вашем счете недостаточно средств!')
#         else:
#             score_sum -= cost
#             name = input('Введите имя покупки: ')
#             history.append((name, cost))
#         return score_sum
#
#
#     while True:
#         print('1. пополнение счета')
#         print('2. покупка')
#         print('3. история покупок')
#         print('4. выход')
#         print(f'На вашем счете {score_sum}')
#
#         choice = input('Выберите пункт меню')
#         if choice == '1':
#             cost = int(input('Введите сумму пополнения: '))
#             score_sum += cost
#         elif choice == '2':
#             score_sum = buy(score_sum)
#         elif choice == '3':
#             print(history)
#         elif choice == '4':
#             break
#         else:
#             print('Неверный пункт меню')


























