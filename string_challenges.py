# -*- coding: utf-8 -*-
# Вывести последнюю букву в слове
word = 'Архангельск'
# print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
# print((word.lower()).count('а'))
            
# Вывести количество гласных букв в слове
count = 0
for i in word.lower():
    if i in 'аоеуюыиэ':
        count += 1
# print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# print(len(sentence.split(' ')))

# Вывести первую букву каждого слова на отдельной строке
# print([word[0] for word in sentence.split(' ')])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
# print(sum(len(word) for word in words) / len(words))
