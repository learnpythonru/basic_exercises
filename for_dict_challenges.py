from collections import Counter
print('Задание 1\n')
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for line in students:
    names.append(line['first_name'])
count = dict(Counter(names))
for key in count:
    print(f'{key}: {count[key]}')


print('\nЗадание 2\n')
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for line in students:
    names.append(line['first_name'])
rare_name = Counter(names).most_common(1)
rare_name = list(rare_name[0])
print(f'Самое частое имя среди учеников: {rare_name[0]}')


print('\nЗадание 3\n')
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for students in school_students:
    names = []
    for line in students:
        names.append(line['first_name'])
    rare_name = Counter(names).most_common(1)
    rare_name = list(rare_name[0])
    print(f'Самое частое имя среди учеников: {rare_name[0]}')


print('\nЗадание 4\n')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for klass in school:
    class_name = klass['class']
    names = []
    for name in klass['students']:
        names.append(name['first_name'])
    boys = []
    girls = []
    for line in names:
        if is_male[line] is True:
            boys.append(line)
        else:
            girls.append(line)
    print(f'Класс {class_name}: девочки {len(girls)}, мальчики {len(boys)}')


print('\nЗадание 5\n')
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
for klass in school:
    class_name = klass['class']
    names = []
    for name in klass['students']:
        names.append(name['first_name'])
    boys = []
    girls = []
    for line in names:
        if is_male[line] is True:
            boys.append(line)
        else:
            girls.append(line)
    if len(boys) > len(girls):
        print(f'Больше всего мальчиков в классе {class_name}')
    else:
        print(f'Больше всего девочек в классе {class_name}')
