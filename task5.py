"""
Решение задачи 5 предпрофессионального экзамена.
Программа открывает файл с данными, генерирует значение хэша
по данным ФИО и заменяет поле id на значение хэша.
В программе реализована функция
generate_hash - генератор значения хэша по строке ФИО
"""

from csv import reader, writer


def generate_hash(fio):
    """
    Функция подсчитывает значение хэша по формуле из задания
    :param fio:
    Строка вида Фамилия Имя Отчество
    :return:
    Целое число - значение хэша
    """
    letters = '_абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    fio = fio.replace(' ', '')
    p = 67
    m = 10 ** 9 + 9
    hash_value = 0
    for i in range(len(fio)):
        s = letters.find(fio[i])
        hash_value = (hash_value + s * (p ** i) % m) % m
    return hash_value


with open('students.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    pupil_data = list(reader(data_file, delimiter=','))
    # Строка с заголовками столбцов
    header_line = pupil_data.pop(0)

for pupil in pupil_data:
    # Сгенерировать хэш
    new_hash = generate_hash(pupil[1])
    # Заменить поле id значением хэша, в виде строки
    pupil[0] = str(new_hash)

with open('students_with_hash.csv', 'w', encoding='utf-8') as data_file:
    data_writer = writer(data_file, delimiter=',')
    # записать данные в файл
    data_writer.writerow(header_line)
    data_writer.writerows(pupil_data)
