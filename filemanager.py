import shutil
import os
import sys
import platform

def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)


def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result


def author_info():
    return 'Yury Ilin'


def quit():
    sys.exit(0)


def create_directory(name_dir):
    if not os.path.exists(f'new{name_dir}'):
        os.mkdir(f'new{name_dir}')
    else:
        print('Такая папка уже существует')


# def delete_directory(name_dir_del):
#     if os.path.exists(f'new{name_dir_del}'):
#         os.rmdir(f'new{name_dir_del}')
#     else:
#         print('Такая папка или файл не найден')


def delete_directory(name_dir_del):
    if os.path.exists(name_dir_del):
        os.rmdir(name_dir_del)
    else:
        print('Такая папка или файл не найден')


def foldernames():
    result2 = []
    for item in os.listdir():
        if os.path.isdir(item):
            result2.append(item)
    return result2


def view_opersystem():
    result3 = []
    for item in platform.uname():
        result3.append(item)
    return result3


def view_folder():
    result4 = []
    for item in os.listdir():
        result4.append(item)
    return result4


def change_dir(new_dir):
    os.chdir(new_dir)
