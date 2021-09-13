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

def name_in_class(input_students: list):
    """
    Функция возвращает словарь вида {Имя:счетчик}
    """
    name_count = {}
    for student in input_students:
        check_name_count = name_count.get(student['first_name'])
        if check_name_count is None:
            name_count[student['first_name']] = 1
        else:
            name_count[student['first_name']] += 1
    return name_count

name_and_count = name_in_class(students)
for name in name_and_count:
    print(f'{name}: {name_and_count[name]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def most_often_name(input_students: list):
    """
    Функция возвращает список наиболее популярных имен
    """
    name_count = name_in_class(input_students)
    max_count = max(name_count.values())
    # на случай если несколько имен с одинаковым счетчиком
    often_name = [student for student in name_count if name_count[student] == max_count]

    return often_name


print(f'Самое популярное имя среди учеников: {", ".join(most_often_name(students))}')  # простая распаковка в f-строке неработает


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
        {'first_name': 'Саша'}
    ],
]


def often_name_each_class(input_school_class):
    """
    Функция возвращает словарь вида {Номер класса:популярные имена}
    """
    class_count = 0
    name_each_class = {}
    for school_class in input_school_class:
        class_count += 1
        name_each_class[class_count] = most_often_name(school_class)
    return name_each_class


class_and_name = often_name_each_class(school_students)
for school_class in class_and_name:
    print(f'Самое частое имя в классе {str(school_class)}: {", ".join(class_and_name[school_class])}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Петя'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
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
def gender_in_class(input_school_class, input_gender):
    """
    Функция возвращает словарь вида {класс:{мальчики:счетчик, девочки:счетчик}}
    """


    class_boys_girls = {}  # словарь вида {класс:{мальчики:счетчик, девочки:счетчик}}

    # формируем список студентов в классе
    for school_class in input_school_class:
        # проверяем в словаре class_boys_girls наличие ключа с номером класса
        if class_boys_girls.get(school_class['class']) is None:
            # если класса нет в словаре то создаем
            class_boys_girls[school_class['class']] = {'мальчики':0, 'девочки':0}

        for student in school_class['students']:
            # проверяем указан ли пол для студента
            try:
                gender = input_gender.get(student['first_name'])
                if gender is None:
                    raise ValueError('пол не указан')
            except ValueError as error:
                print(f"Для студента {student['first_name']} {error}")
                continue            
            
            if gender:
                class_boys_girls[school_class['class']]['мальчики'] += 1
            else:
                class_boys_girls[school_class['class']]['девочки'] += 1

    return class_boys_girls    


class_boys_girls = gender_in_class(school, is_male)
for class_num in class_boys_girls:
    boys = class_boys_girls[class_num]['мальчики']
    girls = class_boys_girls[class_num]['девочки']
    print(f'Класс {class_num}: девочек {girls}, мальчиков {boys}')


# Задание 5
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

class_boys_girls = gender_in_class(school, is_male)
print(class_boys_girls.values())
max_boy = {}
max_girl = {}
for class_num in class_boys_girls:
    if len(max_boy) == 0 and len(max_girl) == 0:
        max_boy[class_num] = class_boys_girls[class_num]['мальчики']
        max_girl[class_num] = class_boys_girls[class_num]['девочки']
        continue
    print(max_boy.values())
    if max_boy.values() < class_boys_girls[class_num]['мальчики']:
        max_boy.clear()
        max_boy[class_num] = class_boys_girls[class_num]['мальчики']
    if max_girl.values() < class_boys_girls[class_num]['девочки']:
        max_boy.clear()
        max_boy[class_num] = class_boys_girls[class_num]['девочки']


print(max_boy, max_girl)


