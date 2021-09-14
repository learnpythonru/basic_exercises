# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
vowels = 'ауоыиэяюёе'
counter = 0
word = 'Архангельск'
for elem in word.lower():
    if elem in vowels:
        counter += 1
print(counter)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for elem in sentence.split():
    if len(elem) == 0:
        continue
    print(elem[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
counter = 0
lst_words = sentence.split()
for word in lst_words:
    counter += len(word)
print(counter // len(lst_words))
