# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom(word=str(input('Введите слово: '))):
    if word == word[::-1]:
        print(f'Слово {word} является палиндромом')
    else:
        print(f'Слово {word} не является палиндромом')



