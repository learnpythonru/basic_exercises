print('Вывести последнюю букву в слове')
word = 'Архангельск'
print(word[-1])


print('Вывести количество букв "а" в слове')
word = 'Архангельск'
print(word.lower().count('а'))


print('Вывести количество гласных букв в слове')
word = 'Архангельск'
vowels = 0
if word.isalpha():
    for letter in 'аеиоуюя':
        vowels += word.lower().count(letter)
print(vowels)

print('Вывести количество слов в предложении')
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


print('Вывести первую букву каждого слова на отдельной строке')
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


print('Вывести усреднённую длину слова в предложении')
sentence = 'Мы приехали в гости'
len_words = 0
for word in sentence.split():
    len_words += len(word)
print(len_words / len(sentence.split()))
