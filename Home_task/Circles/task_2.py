print('Задача 2. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета,
# что числа не помещаются на бумаге.

# Напишите программу, которая считала бы, сколько цифр во вводимом числе.
# Учтите, что программа должна получать только положительные числа и что число 0 имеет одну цифру.

# Пример 1
# Введите число: 58
# Кол-во цифр в числе: 2

# Пример 2
# Введите число: 0
# Кол-во цифр в числе: 1
num =int(input('Введите число: '))
print('Кол-во цифр в числе: ', len(str((num))))
          #С яндекс практикума узнал,пригодилось)



num =int(input('Введите число: '))
count = 0
while num >= 0:
    count += 1
    num = num // 10
    if num == 0:
        break
print('Кол-во цифр в числе: ', count)