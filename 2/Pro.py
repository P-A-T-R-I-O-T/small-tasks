"""
Синтаксис Python. Домашнее Задание. Pro

Задача 1
Выведите на экран следующий паттерн:

@

@ @

@ @ @

@ @ @ @ @

Обратите внимание на пробел между символами. Рекомендуется использовать циклы (любые) для решения данного задания.
"""

dog = ['@', '@', '@', '@']  # Дан список

for i in range(1, len(dog) + 1): # Перебираем индексы элементов списка dog
    if i == 4:
        print(' '.join(dog[:i]), ' '.join(dog[:1])) # Перебирает весь список и добавляет радлелитьль в виде пробела, а так же добавляет 1 символ дополнительно через пробел
    else:
        print(' '.join(dog[:i]), end="\n" * 2)  # Выводим элементы списка dog со первого до 3-го, разделенные пробелом

"""
Задача 2
Выведите на экран следующий паттерн:

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5

6 6 6 6

7 7 7

8 8

9

Обратите внимание на пробел между символами. Рекомендуется использовать циклы (любые) для решения данного задания.
"""


for n in range(1, 10):  # Переберает диапазон значений от 1 до 9 включительно
# Создаём условия для отображения чисел
    if n == 1 or n == 9: # тут условие дложны быти n равняется 1 или 9
        print(n, end="\n" * 2) # Идёт вывод на экран  значения n, а после него идёт два перехода на следующую строчку
    elif n == 2 or n == 8:
        print(' '.join([str(n)] * 2), end="\n" * 2) # вывод на экран значения n, перед этим преобразуется её в строчку и делает разделитьль пробел и умножает значение на 2 и вконце двойной переход на следующую строчку
    elif n == 3 or n == 7:
        print(' '.join([str(n)] * 3), end="\n" * 2)
    elif n == 4 or n == 6:
        print(' '.join([str(n)] * 4), end="\n" * 2)
    else:
        print(' '.join([str(n)] * 5), end="\n" * 2)


"""
Задача 3
Используя цикл while, выведите на экран таблицу умножения для числа 7.

Пример

Для числа 5 выдача выглядит так:

5 * 1 = 5

5 * 2 = 10

5 * 3 = 15

5 * 4 = 20

5 * 5 = 25

...

5 * 9 = 45
"""
n = 1 # Второй множитель
i = 7 # Первый множитель
while n <= 9: # Запускаем цикл и делаем ограничение для второго числителя до 9 включительно
    u = i * n # Производим вычисление и записываем результат в переменную u
    print(i,'*',n,'=',u) # Выводим пример с результатом на экран
    n += 1 # Прибавляем 1 ко второму числителю


"""
Задача 4
Представьте, что вы подбрасываете два кубика одновременно.
Считайте с входящей строки два целых числа d1 и d2. Проверьте,
соответсуют ли введенные числа интервалу значений для кубика.
Если нет, то выведите на экран строку "Ошибка!
Значение на кубике (1 или 2, вставьте подходящее значение) не входит в интервал [1, 6]".
В противном случае посчитайте сумму выпавших значений.
Если сумма равна 7 или 11, выведите на экран "Я победил!!!".
Если сумма равна 2, 3 или 12, то выведите на экран "Я проиграл :
(" Во всех остальных случаях выведите на экран сумму значений.
"""
d1 = int(input('Введите первое целое число: '))
d2 = int(input('Введите второе целое число: '))

if d1 not in range(1, 7) or d2 not in range(1, 7):
    print("Ошибка!Значение на кубике (1 или 2, вставьте подходящее значение) не входит в интервал [1, 6]")
else:
    if d1 + d2 == 7 or d1 + d2 == 11:
        print("Я победил!!!")
    elif d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12:
        print("Я проиграл")
    else:
        print(d1 + d2)



"""

Задача 5
Напишите код, который ищет все числа в интервале от 3000 до 4300 включительно,
делящиеся на 11, но не делящиеся на 5. Выведите на экран все найденные числа.
"""
for i in range(3000, 4301): # Создали цикл который будет перебирать все значения в указанном диапазон
    if i % 11 == 0: # Условие если число значения i делиться на 11 без остатка
        if i % 5 != 0: # Условие сли число значения i не делиться на 5 без остатка
            print(i) # Выводим все значения из указанного выше диапазона при условии что оба условия выши верны
