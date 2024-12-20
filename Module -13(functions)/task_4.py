print('Задача 4. Текстовый редактор')

# Продолжаем разрабатывать новый текстовый редактор.
# Теперь нам поручили написать для него код, который считает, сколько раз в тексте встречается любая выбранная буква
# или цифра (а не только буква «ы», как было в задаче 3 урока «Цикл for: итерирование по строке»).

# Что нужно сделать
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и букв N.
# Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Пример
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters():
    num_count = 0
    word_count = 0
    for a in str(text):
        if str(a) == str(num):
            num_count += 1
        elif str(a) == str(word):
            word_count +=1
    print('Количество цифр ', num,' :', num_count)
    print('Количество букв ', word,' :', word_count)



text =str(input('Введите текст: '))
num =str(input('Какую цифру ищем? '))
word =str(input('Какую букву ищем? '))
count_letters()