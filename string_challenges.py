# Вывести последнюю букву в слове
word = 'Архангельск'
print(list(word)[-1])
#print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(list(word).count('а'))
print(list(word.lower()).count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
letters = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
new_lst=[]
 
for vowels in word.lower():
    if vowels in letters:
        new_lst.append(vowels)
 
print(f'В этой строке содержаться  {len(new_lst)} гласных букв')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'В предложении {len(sentence.split())} слова')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print (word[0])



# Вывести усреднённую длину слова в предложении. Посчитать и сложить длины каждого слова, разделить на количество слов)
sentence = 'Мы приехали в гости'

avg_word = len(sentence.replace(" ", "")) / len((sentence.split()))
print(avg_word)