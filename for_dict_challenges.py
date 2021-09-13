from collections import Counter, defaultdict
from rich import print

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students_task1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


def print_names_and_count(students):
    counter = defaultdict(int)

    for student in students:
        name = student['first_name']
        counter[name] += 1

    for name in counter:
        name_count = counter[name]
        print(f'{name}: {name_count}')

# created separated functions
# print_names_and_count() with task1_solution()
# to have more context


def task1_solution(students_task1):
    print_names_and_count(students_task1)

# task1_solution(students_task1)

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша


students_task2 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def define_frequent_name(students):
    counter = defaultdict(int)

    for student in students:
        name = student['first_name']
        counter[name] += 1

    print(f'Самое частое имя среди учеников: {max(counter, key=counter.get)}')


def task2_solution(students):
    define_frequent_name(students)

# task2_solution(students_task2)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


school_students_task3 = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


def count_names_in_school(school_students):
    counter = defaultdict(int)

    for school_class in school_students:
        for pupil in school_class:
            name = pupil['first_name']
            counter[name] += 1

    for pupil in counter:
        school_class = list(counter).index(pupil)
        print(f'Самое частое имя в {school_class + 1} классе: {pupil}')


def task3_solution(school_students_task3):
    count_names_in_school(school_students_task3)

# task3_solution(school_students_task3)

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2


school_task4 = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {
        'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

is_male_task4= {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def task4_solution(school, is_male):
    for school_class in school:
        school_class_number = school_class['class']
        students = school_class.get('students')
        
        # creating default dict to store 
        # number of girls and boys
        # do we actually need defaultdict or
        # we can user usual dict?
        genders = defaultdict(int)
        genders['male'] = 0
        genders['female'] = 0

        for student in students:
            name = student.get('first_name')
            if is_male.get(name) == True:
                genders['male'] += 1
            elif is_male.get(name) == False:
                genders['female'] += 1
                
        print(f'В классе {school_class_number}: девочки: {genders["female"]}, мальчики {genders["male"]}')
        
# task4_solution(school_task4, is_male_task4)

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

# school_task5 = [
#     {'class': '2a', 'students': [
#         {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#     {'class': '3c', 'students': [
#         {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]

school_task5 = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '3a', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

is_male_task5 = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def test(is_male, school_task):
    male_count = defaultdict(int)
    female_count = defaultdict(int)
    for school_class in school_task:
        # male_count = defaultdict(int)
        # female_count = defaultdict(int)
        students = school_class.get('students')
        school_class_number = school_class.get('class')
        
        for student in students:
            name = student.get('first_name')
            if is_male.get(name) == True:
                male_count[school_class_number] += 1
            elif is_male.get(name) == False:
                female_count[school_class_number] += 1  
                      
    female_class = max(female_count, key=female_count.get)
    male_class = max(male_count, key=male_count.get)
    print(f'Класс с самым большим количеством мальчиков: {male_class}')
    print(f'Класс с самым большим количеством девочек: {female_class}')

test(is_male_task5, school_task5)