
# Вывести последнюю букву в слове
from typing import Counter


word = 'Архангельск'
# ???
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(f'{Counter(word.lower())}')


# Вывести количество гласных букв в слове
word = 'Arkhangelsk'
count = 0
for letter in word:
    if letter.lower() in 'aeiou':
        count += 1
print(f'кол-во букв в слове {word}: {count}')


# ???

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
    print(f'{word[0].lower()}')
print('______')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
words = sentence.split()
print(word)
average = sum(len(word) for word in words) /  len(sentence.split())
print(average)

 