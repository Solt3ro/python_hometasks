print('Задача 4. Среднее на отрезке')
a =int(input('Введите первое число: '))
b =int(input('Введите второе число: '))
c =int(input('Введите третье число: '))
for mid in range(a, b -1,):
    if ((mid + mid)/2) % c ==0:
        print('Число из отрезка', a,'-', b, ', кратное числу', c,': =', mid)