# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

# names1 = ['Оля', 'Петя', 'Вася', 'Маша']

# def print_names(list):
#     for name in list:
#         print(name)

# print_names(names1)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

# def print_and_count_letters(list):
#     for name in list:
#         print(f'{name}: {len(name)}')

# names2 = ['Оля', 'Петя', 'Вася', 'Маша']

# print_and_count_letters(names2)

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

# is_male = {
#     'Оля': False,  # если False, то пол женский
#     'Петя': True,  # если True, то пол мужской
#     'Вася': True,
#     'Маша': False,
# }
# names = ['Оля', 'Петя', 'Вася', 'Маша']

# def define_gender(names_and_genders):     
#     for name in names_and_genders:
#        gender = names_and_genders[name]
#        print(gender)
    
#        if gender == True:
#            print('male')
#            return 'male'
#        elif gender == False:
#            print('female')
#            return 'female'

# define_gender(is_male)

# def print_names_and_gender(list):
#     for name in list:
#         print(f'{name}: {define_gender(list)}')

# print_names_and_gender(is_male)

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

# groups = [
#     ['Вася', 'Маша'],
#     ['Вася', 'Маша', 'Саша', 'Женя'],
#     ['Оля', 'Петя', 'Гриша'],
# ]

# def print_groups(groups):
#     for group in groups:
#         group_number = groups.index(group) + 1
#         pupil_number = len(group)
#         print(f'Группа {group_number}: {pupil_number} учеников')

# print_groups(groups)

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

# groups = [
#     ['Вася', 'Маша'],
#     ['Оля', 'Петя', 'Гриша'],
#     ['Вася', 'Маша', 'Саша', 'Женя'],
# ]

# def print_groups(groups):
#     for group in groups:
#         group_number = groups.index(group) + 1
#         names = ', '.join(group)
#         print(f'Группа {group_number}: {names}')

# print_groups(groups)