# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import defaultdict
from typing import Counter


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???

names = [name['first_name'] for name in students]
count = Counter(names)
for name, number in count.items():
    print(f'{name}: {number}')
print('____')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'}
]
names_list = [name['first_name'] for name in students]
name_count = {name: names_list.count(name) for name in names_list}
max_count = max(name_count[name] for name in name_count)

if name_count[name] == max_count:
    print(f'Самое частое имя среди учеников: {name}')

# print(Counter(name_count).most_common(1))
print(f'Самое частое имя среди учеников: {Counter(name_count).most_common(1)[0][0]}')

# Задание 3
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
# ???

for idx, each_class in enumerate(school_students,1):
    class_list = [name['first_name'] for name in each_class]
    print(f'Самое частое имя среди учеников класса {idx} : {Counter(class_list).most_common(1)[0][0]}')


# Задание 4
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
# ???


for class_at_school in school:
    boys = 0
    girls = 0
    for student in class_at_school['students']:
        for name in student.values():
            if is_male[name] == True:
                boys += 1
            else: 
                girls += 1


    print(f'Класс {class_at_school["class"]} : мальчики: {boys} девочки: {girls}') 
print("___")
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name':'Сережа'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Сережа': True
}
# ???
list_of_class = []
for class_at_school in school:
    class_genders = {'class': class_at_school['class'], 'boy': 0, 'girl': 0 }
    boys = 0
    girls = 0
    list_of_class.append(class_genders)
    for student in class_at_school['students']:
        for name in student.values():
            if is_male[name] == True:
                class_genders['boy'] += 1
            else: 
                class_genders['girl'] += 1

max_boys = 0
max_girls = 0                
for class_with_max_boys in list_of_class:
    if class_with_max_boys['boy'] > max_boys:
        max_boys = class_with_max_boys['boy']
        class_max_boys = class_with_max_boys['class']
print(f'Больше всего мальчиков в классе {class_max_boys}: {max_boys} мальчика')
for class_with_max_girls in list_of_class:     
    if class_with_max_girls['girl'] > max_girls:
        max_girls = class_with_max_girls['girl']
        class_max_girls = class_with_max_girls['class']
print(f'Больше всего девочек в классе {class_max_girls}: {max_girls} девочек')       
