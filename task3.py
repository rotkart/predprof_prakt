"""
Решение задачи 3 предпрофессионального экзамена.
Программа читает данные из файла.
Далее в бесконечном цикле запрашивает номер проекта и
ищет его линейным поиском.
Выход из цикла - по значению СТОП
"""

from csv import reader

with open('students.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    pupil_data = list(reader(data_file, delimiter=','))
# Ввод первого значения
project_id = input('Введите номер проекта или СТОП: ')
# Цикл до ввода СТОП
while project_id != 'СТОП':
    # Линейный поиск позиции искомого значения
    position = -1
    for i in range(len(pupil_data)):
        if pupil_data[i][2] == project_id:
            position = i
            break
    # Вывод на экран
    if position > 0:
        pupil_name = pupil_data[position][1].split()
        name = pupil_name[1][0] + '.' + pupil_name[0]
        print(f'Проект No {project_id} делал: {name} он(а) получил(а) оценку - {pupil_data[position][4]}.')
    else:
        print('Ничего не найдено.')
    # Чтение следующего значения
    project_id = input('Введите номер проекта или СТОП: ')
