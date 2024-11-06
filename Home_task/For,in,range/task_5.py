print('Задача 5. Замечательные числа')

# Напишите программу, которая находит и выводит все двузначные числа, равные утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.
# Так, число 15 подходит, поскольку 1 * 5 * 3 = 15, то есть мы разбили число 15 на цифры 1 и 5, после чего получили утроенное произведение.

# Подсказка: чтобы найти утроенное произведение числа, разделите его на отдельные цифры, перемножьте их, а затем умножьте полученный результат на 3.

# Пример
# Замечательные числа в диапазоне двузначных:
# 15
# 24
for a in range(100+1):
    if a == ((a //10) * (a %10) * 3):
        print(a)