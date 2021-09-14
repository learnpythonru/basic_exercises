# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names1 = ['Оля', 'Петя', 'Вася', 'Маша']

def task1_solution(list):
    for name in list:
        print(name)

# unprint to see solution of first task
# task1_solution(names1)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

def task2_solution(list):
    for name in list:
        print(f'{name}: {len(name)}')

names2 = ['Оля', 'Петя', 'Вася', 'Маша']

# uncomment to see task 2 solution
# task2_solution(names2)

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male_task3 = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names_task3 = ['Оля', 'Петя', 'Вася', 'Маша']

def task3_solution(names, genders):     
    for name in names:
       gender = genders.get(name)
    
       if gender == True:
           print(f'{name}: Мужской пол')
       elif gender == False:
           print(f'{name}: Женский пол')

# uncomment to see task 3 solution
# task3_solution(is_male_task3)

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups_task4 = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

def task4_solution(groups):
    for group in groups:
        group_number = groups.index(group) + 1
        pupil_number = len(group)
        print(f'Группа {group_number}: {pupil_number} учеников')

# uncomment to see task 4 solution
# task4_solution(groups_task4)

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups_task5 = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

def task5_solution(groups):
    for group in groups:
        group_number = groups.index(group) + 1
        names = ', '.join(group)
        print(f'Группа {group_number}: {names}')

# uncomment to see task 5 solution
# task5_solution(groups_task5)