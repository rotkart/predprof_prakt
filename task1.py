"""
Решение задачи 1 предпрофессионального экзамена.
Программа читает данные из csv-файла, ищет результат конкретного учащегося.
Затем подсчитывает средний балл, заменяет им результаты None
и сохраняет в новый файл.
"""

from csv import reader, writer

# Выполнение 1-й части задания
with open('students.csv', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter=',')
    # Линейным поиском получить ответ
    for row in csv_data:
        if "Хадаров Владимир" in row[1]:
            print(f'Ты получил: {row[4]}, за проект - {row[2]}')

# Вторая часть задания
with open('students.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    pupil_data = list(reader(data_file, delimiter=','))
    # Строка с подписями столбцов
    header_line = pupil_data.pop(0)
    # Словарь класс:[кол-во учащихся, сумма оценок]
    school_classes = dict()
    for pupil in pupil_data:
        class_name = pupil[3]
        grade = pupil[4]
        if class_name not in school_classes.keys():
            school_classes[class_name] = [0, 0]
        if grade != 'None':
            school_classes[class_name][0] += 1
            school_classes[class_name][1] += int(grade)
    # Замена оценок None на среднюю по классу
    for pupil in pupil_data:
        if pupil[4] == 'None':
            average_grade = school_classes[pupil[3]][1] / school_classes[pupil[3]][0]
            # В OO Calc разделитель дробной части - запятая
            pupil[4] = str(round(average_grade, 3)).replace('.', ',')

with open('students_new.csv', 'w', encoding='utf-8') as data_file:
    # Запись в объект writer
    data_writer = writer(data_file, delimiter=',')
    # Строка с подписями столбцов
    data_writer.writerow(header_line)
    # Список строк с исправленными оценками
    data_writer.writerows(pupil_data)
