# Задание 1
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

names_dict = {}
for i in students:
    name = i['first_name']
    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

for name in names_dict:
    print(f'{name}: {names_dict[name]}')


# Задание 2
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


names_dict = {}
for i in students:
    name = i['first_name']
    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

most_frequent_name = sorted(names_dict.items(), key=lambda x: x[1], reverse=True)[0]
print(f'Самое частое имя среди учеников: {most_frequent_name[0]}')



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

for cls in school_students:
    names_dict = {}
    for i in cls:
        name = i['first_name']
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1

    most_frequent_name = sorted(names_dict.items(), key=lambda x: x[1], reverse=True)[0]
    print(f'Самое частое имя в классе {school_students.index(cls) + 1}: {most_frequent_name[0]}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for cls in school:
    girls = 0
    boys = 0
    for student in cls['students']:
        name = student.get('first_name')
        if is_male[name]:
            boys += 1
        else:
            girls += 1

    print(f'Класс {cls["class"]}: девочки {girls}, мальчики {boys}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}, {'first_name': 'Олег'},]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]}
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Даша': False
}

# 'class': [girls, boys]
max_girls_class = ['', 0]
max_boys_class = ['', 0]
  

for cls in school:
    girls = 0
    boys = 0

    for student in cls['students']:
        name = student.get('first_name')
        if is_male[name]:
            boys += 1
        else:
            girls += 1

    if girls > max_girls_class[1]:
        max_girls_class[0] = cls['class']
        max_girls_class[1] = girls
    
    if boys > max_boys_class[1]:
        max_boys_class[0] = cls['class']
        max_boys_class[1] = boys

print(f'Больше всего девочек в классе {max_girls_class[0]}')
print(f'Больше всего мальчиков в классе {max_boys_class[0]}')
