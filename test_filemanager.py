from filemanager import *
import os
import platform
from game_function import *
import random

def test_filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    assert filenames() == result


def test_author_info():
    assert author_info() == 'Yury Ilin'


def test_create_directory():
    os.mkdir('name_dir')
    assert 'name_dir' in os.listdir()


def test_delete_directory():
    # os.mkdir('name_dir')
    assert delete_directory('name_dir') not in os.listdir()


def test_foldernames():
    result2 = []
    for item in os.listdir():
        if os.path.isdir(item):
            result2.append(item)
    assert foldernames() == result2


def test_view_opersystem():
    result3 = []
    for item in platform.uname():
        result3.append(item)
    assert view_opersystem() == result3


def test_view_folder():
    result4 = []
    for item in os.listdir():
        result4.append(item)
    assert view_folder() == result4


def test_date_to_str():
    assert date_to_str('29.01.1860') == 'двадцать девятое января 1860 года'


def test_run_victory():
    # кол-во возвращаемых элементов списка
    FAMOUS = {'Чехов': '29.01.1860', 'Высоцкий': '25.01.1938', 'Менделеев': '08.02.1834',
                  'Крылов': '13.02.1769', 'Ушаков': '24.02.1744', 'Гагарин': '09.03.1934',
                  'Чуковский': '31.03.1882', 'Смоктуновский': '28.03.1925', 'Шаляпин': '13.02.1873',
                  'Матросов': '05.02.1924'
                  }
    random_famous = random.sample(FAMOUS.keys(), 5)
    assert len(random_famous(FAMOUS, 5)) == 5


