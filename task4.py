"""
Решение задачи 4 предпрофессионального экзамена.
Программа читает файл с данными, для каждого ученика генерирует имя
пользователя и пароль, дополняя имеющиеся данные.
Новые данные сохраняются в файл csv.
В программе реализованы функции:
generate_login - для преобрадования ФИО в логин нужного формата
generate_password - для генерации пароля по установленным правилам
"""

from random import shuffle, sample
from csv import reader, writer


def generate_login(string):
    """
    Функция генерирует логин из строки с ФИО вида Фамилия и инициалы.
    :param string:
    Фамилия Имя Отчество - строка с разделителем пробел
    :return:
    Строка вида Фамилия_ИО
    """
    fio = string.split()
    login = fio[0] + '_' + fio[1][0]
    if len(fio) > 2:
        login += fio[2][0]
    return login


def generate_password(length):
    return ""


with open('students.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    pupil_data = list(reader(data_file, delimiter=','))
    header_line = pupil_data.pop(0)

for pupil in pupil_data:
    login = generate_login(pupil[1])
    password = generate_password(8)
    pupil.append(login)
    pupil.append(password)

with open('students_password.csv', 'w', encoding='utf-8') as data_file:
    data_writer = writer(data_file, delimiter=',')
    header_line.append('login')
    header_line.append('password')
    data_writer.writerow(header_line)
    data_writer.writerows(pupil_data)
