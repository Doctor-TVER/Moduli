"""В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.

Описание пунктов:
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;
- посмотреть только папки
вывод только папок которые находятся в рабочей папке;
- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке;
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
- играть в викторину
запуск игры викторина из предыдущего дз;
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
- выход
выход из программы.
Так же можно добавить любой другой интересный или полезный функционал по своему желанию
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход"""

"""
Модуль для запуска консольного файлового менеджера
"""

# Функции файлового менеджера
import filemanager
# Мой счет
from my_bank import run_bill
# Викторина
from game_function import run_victory
import os

# Названия пунктов меню
CREATE_FOLDER = 'Создать папку'
DELETE_FOLDER = 'Удалить файл/папку'
COPY_FILE_FOLDER = 'Копировать (файл/папку)'
VIEWING_FOLDER = 'Просмотр содержимого рабочей директории'
SAVE_WORK_DIR_TO_FILE = 'Cохранить содержимое рабочей директории в файл'
SHOW_FOLDER = 'Посмотреть только папки'
SHOW_FILES = 'Посмотреть только файлы'
VIEW_OPER_SYSTEM = 'Просмотр информации об операционной системе'
AUTHOR = 'Создатель программы'
VICTORY = 'Играть в викторину'
BILL = 'Мой банковский счет'
CHANGE_WORK_FOLDER = 'Cмена рабочей директории'
EXIT = 'Выход'

# Набор пунктов меню
menu_items = (
    CREATE_FOLDER,
    DELETE_FOLDER,
    COPY_FILE_FOLDER,
    VIEWING_FOLDER,
    SAVE_WORK_DIR_TO_FILE,
    SHOW_FOLDER,
    SHOW_FILES,
    VIEW_OPER_SYSTEM,
    AUTHOR,
    VICTORY,
    BILL,
    CHANGE_WORK_FOLDER,
    EXIT
)


def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count



def create_a_folder():
    name_dir = input('Введите название папки: ')
    filemanager.create_directory(name_dir)


def delete_a_folder():
    name_dir_del = input('Введите название папки или файла: ')
    filemanager.delete_directory(name_dir_del)



def copy_file_or_folder():
    """
    Копирование файла или папки
    :return:
    """
    # спрашиваем имя и новое имя
    name = input('Введите имя файла')
    new_name = input('Введите имя копии')
    # копируем
    filemanager.copy_file_or_directory(name, new_name)


def print_author():
    """
    Функция печати информации об авторе
    :return:
    """
    # получаем информацию
    author = filemanager.author_info()
    # печатаем
    print(author)


def print_files():
    """
    Функция печати файлов в рабочей папке
    :return: None
    """
    # Получаем файлы
    files = filemanager.filenames()
    # Выводим
    for item in files:
        print(item)


def print_folder():
    """
    Функция печати папок в рабочей папке
    :return: None
    """
    # Получаем файлы
    folders = filemanager.foldernames()
    # Выводим
    for item in folders:
        print(item)


def view_directory():
    content = filemanager.view_folder()
    for item in content:
        print(item)


def view_operation_system():
    info_sys = filemanager.view_opersystem()
    for item in info_sys:
        print(item)


def change_work_dir(new_dir):
    new_dir = input('Введите путь к папке: ')
    filemanager.change_dir(new_dir)


def save_work_dir():
    CONTENT_DIR = 'listdir.txt'
    save_file = []
    save_folder = []
    with open(CONTENT_DIR, 'w') as f:
        for item in os.listdir():
            if os.path.isfile(item):
                save_file.append(item)
            else:
                save_folder.append(item)
    with open(CONTENT_DIR, 'r') as f:

        for order in f:
            print(f'files: {save_file}')
            print(f'dirs: {save_folder}')
    print(f'files: {save_file}')
    print(f'dirs: {save_folder}')


# Словарь действия связывает название пункта меню с той функцией которую нужно выполнить
actions = {
    CREATE_FOLDER: create_a_folder,
    DELETE_FOLDER: delete_a_folder,
    COPY_FILE_FOLDER: copy_file_or_folder,
    VIEWING_FOLDER: view_directory,
    SAVE_WORK_DIR_TO_FILE: save_work_dir,
    SHOW_FOLDER: print_folder,
    SHOW_FILES: print_files,
    VIEW_OPER_SYSTEM: view_operation_system,
    AUTHOR: print_author,
    VICTORY: run_victory,
    BILL: run_bill,
    CHANGE_WORK_FOLDER: change_work_dir,
    EXIT: filemanager.quit
}


def print_menu():
    """
    Функция вывода меню
    :return: None
    """
    print(separator())
    # Выводим название пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 1):
        print(f'{number}) {item}')
    print(separator())


def is_correct_choice(choice):
    """
    Функция проверяет что выбран корректный пункт меню
    :param choice: выбор
    :return: True/False
    """
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)


if __name__ == '__main__':
    # цикл основной программы
    while True:
        # рисуем меню
        print_menu()
        # пользователь выбирает цифру
        choice = input('Выберите пункт меню ')
        # проверяем что это корректный выбор
        if is_correct_choice(choice):
            # получаем назвнание пункта меню по номеру
            # choice - 1, т.к. в меню пункты выводятся с 1 а в картеже хранятся с 0
            choice_name = menu_items[int(choice) - 1]
            # получаем действие в зависимости от пунктам меню
            action = actions[choice_name]
            # вызываем функцию
            action()
        else:
            print('Неверный пункт меню')
# import os
# import platform
# import shutil
# import game_function
# while True:
#     print('1. создать папку')
#     print('2. удалить (файл/папку)')
#     print('3. копировать (файл/папку)')
#     print('4. просмотр содержимого рабочей директории')
#     print('5. посмотреть только папки')
#     print('6. посмотреть только файлы')
#     print('7. просмотр информации об операционной системе')
#     print('8. создатель программы')
#     print('9. играть в викторину')
#     print('10. мой банковский счет')
#     print('11. смена рабочей директории')
#     print('12. выход')
#     # print(f'На вашем счете {score_sum}')
#
#     choice = input('Выберите пункт меню')
#     if choice == '1':
#         name_dir = input('Введите название папки: ')
#             # проверка на существование
#         if not os.path.exists(f'new{name_dir}'):
#                 # сздать папку передаем путь
#             os.mkdir(f'new{name_dir}')
#         else:
#             print('Такая папка уже существует')
#
#     elif choice == '2':
#         name_dir_del = input('Введите название папки или файла: ')
#         if  os.path.exists(f'new{name_dir_del}'):
#             os.rmdir(f'new{name_dir_del}')
#         else:
#             print('Такая папка или файл не найден')
#     elif choice == '3':
#         real_dir = input('Введите название папки или файла, который копируем: ')
#         copy_dir = input('Введите новое название папки или файла: ')
#         shutil.copytree(real_dir, copy_dir)
#     elif choice == '4':
#         print(os.listdir())
#     elif choice == '5':
#         print(os.listdir())
#         for something in os.listdir():
#             if os.path.isdir(something):
#                 print(something)
#     elif choice == '6':
#         print(os.listdir())
#         for something in os.listdir():
#             if os.path.isfile(something):
#                 print(something)
#     elif choice == '7':
#         print(platform.uname())
#     elif choice == '8':
#         print('Создатель программы - Юрик')
#     elif choice == '9':
#         game_function.victory()
#     elif choice == '10':
#         game_function.my_bank_score()
#     elif choice == '11':
#         new_dir = input('Введите путь к папке: ')
#         os.chdir(new_dir)
#     elif choice == '12':
#          break
#     else:
#          print('Неверный пункт меню')