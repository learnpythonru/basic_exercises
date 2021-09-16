from collections import Counter


IS_MALE = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def get_max_count_name(input_lst: list) -> str:
    names = Counter([student['first_name'] for student in input_lst])
    return max(names, key=names.get)


def get_gender_counter(input_lst: list) -> Counter:
    lst_genders = ['male' if IS_MALE[elem['first_name']] else 'female' for elem in input_lst]
    return Counter(lst_genders)


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

names = Counter([student['first_name'] for student in students])
for name, counter in names.items():
    print(f'{name}: {counter}')


# # Задание 2
# # Дан список учеников, нужно вывести самое часто повторяющееся имя
# # Пример вывода:
# # Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
max_count_name = get_max_count_name(students)
print(f'Самое частое имя среди учеников: {max_count_name}')


# # Задание 3
# # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# # Пример вывода:
# # Самое частое имя в классе 1: Вася
# # Самое частое имя в классе 2: Маша

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

for index, students in enumerate(school_students):
    max_count_name = get_max_count_name(students)
    print(f'Самое частое имя в классе {index + 1}: {max_count_name}')


# # # Задание 4
# # # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# # # Пример вывода:
# # # Класс 2a: девочки 2, мальчики 0
# # # Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

for cls in school:
    counter_genders = get_gender_counter(cls['students'])
    print(f"Класс {cls['class']}: девочки {counter_genders.get('female', 0)}, " +
          f"мальчики {counter_genders.get('male', 0)}")

# # # Задание 5
# # # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# # # Пример вывода:
# # # Больше всего мальчиков в классе 3c
# # # Больше всего девочек в классе 2a

school = [
   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

count_lst = []
for cls in school:
    counter_genders = get_gender_counter(cls['students'])
    count_lst.append({'class': cls['class'], 'genders': counter_genders})

max_male_elem = max(count_lst, key=lambda x: x['genders']['male'])
max_female_elem = max(count_lst, key=lambda x: x['genders']['female'])

print(f"Больше всего мальчиков в классе {max_male_elem['class']}")
print(f"Больше всего девочек в классе {max_female_elem['class']}")
