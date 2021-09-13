from typing import Any, List


def generate_name_list(input_lst: List[Any]) -> list:
    return [student['first_name'] for student in input_lst if 'first_name' in student]


def get_max_count_name(input_lst: List[Any]) -> int:
    names = generate_name_list(input_lst)
    count_names: dict = {name: names.count(name) for name in set(names)}
    return max(count_names, key=count_names.get)


def get_gender_count(input_lst: list) -> dict:
    names = generate_name_list(input_lst)
    gender_dict = {'male': 0, 'female': 0}
    for name in names:
        if not (name in is_male.keys()):
            continue
        if is_male[name]:
            gender_dict['male'] += 1
        else:
            gender_dict['female'] += 1
    return gender_dict

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

names = generate_name_list(students)


for name in set(names):
    print(f'{name}: {names.count(name)}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
max_count_name = generate_name_list(students)
print(f'Самое частое имя среди учеников {max_count_name}')


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
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for (index, students) in enumerate(school_students):
    max_count_name = get_max_count_name(students)
    print(f'Самое частое имя в классе {index + 1}: {max_count_name}')


# # Задание 4
# # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# # Пример вывода:
# # Класс 2a: девочки 2, мальчики 0
# # Класс 2б: девочки 0, мальчики 2

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

for cls in school:
    if not ('students' in cls.keys()):
        continue
    gender_dict = get_gender_count(cls['students'])
    print(f"Класс {cls['class']}: девочки {gender_dict['female']}, мальчики {gender_dict['male']}")


# # Задание 5
# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# # Пример вывода:
# # Больше всего мальчиков в классе 3c
# # Больше всего девочек в классе 2a

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

count_array = []
for cls in school:
    if not ('students' in cls.keys()):
        continue
    gender_dict = get_gender_count(cls['students'])
    gender_dict['class'] = cls['class']
    count_array.append(gender_dict)

    max_male_elem = max(count_array, key=lambda x: x['male'])
    max_female_elem = max(count_array, key=lambda x: x['female'])

    print(f"Больше всего мальчиков в классе {max_male_elem['class']}")
    print(f"Больше всего девочек в классе {max_female_elem['class']}")
