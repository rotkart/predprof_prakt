"""
Решение задачи 2 предпрофессионального экзамена.
Программа читает файл данных и сортирует его по графе score
при помощи сортировки вставками.
Затем выводятся трое победителей каждого 10 класса.
"""

from csv import reader

with open('student.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    pupil_data = list(reader(data_file, delimiter=','))
    # Строка с подписями столбцов
    header_line = pupil_data.pop(0)
    # Реализация сортировки вставками
    for i in range(1, len(pupil_data)):
        # Текущий элемент
        elem = pupil_data[i]
        # Поиск места вставки и сдвиг всех значений больше текущего
        j = i
        while j > 0 and pupil_data[j - 1][4] > elem[4]:
            pupil_data[j] = pupil_data[j - 1]
            j -= 1
        # Вставка значения
        pupil_data[j] = elem
        # Вывод результата в нужном формате
    print("10 класс")
    for i in range(3):
        pupil_name = pupil_data[-1 - i][1].split()
        name = pupil_name[1][0] + '.' + pupil_name[0]
        print(f'{i + 1} место: {name}')
