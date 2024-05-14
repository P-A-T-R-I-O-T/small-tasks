from math import sin as sinus

# Домашнее задание
# Функции и модули

# Ultra light
# Задача 1

# Напишите функцию, которая будет выводить количество букв в слове.
# Проверьте при помощи этой функции,

# сколько букв в слове восьмидесятивосьмимиллиметровое.

def number_of_letters(a_little_counting):
    if len(a_little_counting) == 0:
        a_little_counting = 'восьмидесятивосьмимиллиметровое'
        print(len(a_little_counting))
    else:
        print(len(a_little_counting))


a_little_counting = str(input('Введите слово: '))
number_of_letters(a_little_counting)



#Задача 2

# Напишите функцию, которая выводит таблицу умножения (от 1 до 9)
# для указанного числа в следующем формате:
"""
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
...
9 * 3 = 27
"""

def multiplication(x):
    z = 0
    for y in range(1, 10):
        z = y * x
        print(y, '*', x, '=', z)

x = int(input("Введите число: "))
multiplication(x)

# Задача 3

#Напишите функцию, которая выводит сумму,
# разность и произведение двух,
# поданных на вход чисел.

def calculator(x, y):
    print(x + y)
    print(x / y)
    print(x * y)

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
calculator(x, y)



# Задача 4

# Импортируйте функцию sin из модуля math
# с присвоением ей псевдонима sinus.
# Посчитайте при помощи импортированной функции,
# чему будет равен синус единицы.

print('Sinus = ', sinus(1))

# Задача 5

#Напишите лямбда-функцию, которая считает куб числа.

counting_the_cube = lambda a: a**3

a = int(input('Введите число, который нужно возвести в куб: '))
print(counting_the_cube(a))

print((lambda a: a**3)(a))