import numpy as np
"""
Numpy. Домашнее Задание. Pro
Задача 1

Подгрузите массив с файла iris.csv и назовите этот массив my_array.
Создайте двумерный массив из случайных чисел той же размерности,
что и my_array (раздел "Семплирование из распределений",
потребуется использовать размерность массива my_array).
Назовите его my_generated_array.
"""
my_array = np.loadtxt('iris.csv', delimiter=',', skiprows=1)
my_generated_array = np.random.random(my_array.shape)
print(my_generated_array.shape)
print(my_array.shape)


"""
Задача 2
Выполните поэлементное умножение my_array на my_generated_array (раздел "Векторные операции").
Склейте массивы my_array, my_generated_array в один (могут помочь методы np.concatenate, np.vstack, np.hstack).
Возьмите склеенный массив и разделите его на равные части (больше двух).
Можно сделать вручную через циклы либо воспользоваться методом vsplit.
"""
rezult = my_array * my_generated_array


# np.concatenate: Этот метод объединяет массивы вдоль определенной оси.
# Мы можем указать ось, по которой хотим объединить массивы.
# По умолчанию ось равна 0, что означает объединение по вертикали.
# Метод np.concatenate позволяет объединять массивы по любой оси.
concatenated_array = np.concatenate((my_array, my_generated_array), axis=0) # Склеиваем С использованием np.concatenate
print("\n" * 2, concatenated_array.shape)
parts = np.vsplit(concatenated_array, 3) # Разделяем массив на 3 равные части
part1, part2, part3 = parts # Сохраняем каждую часть в отдельную переменную
# Выводим форму каждой части
print("Форма части 1:", part1.shape)
print("Форма части 2:", part2.shape)
print("Форма части 3:", part3.shape)



# np.vstack: Этот метод используется для вертикальной стыковки массивов.
# Он объединяет массивы вдоль вертикальной оси (по строкам)
array_vstack = np.vstack((my_array, my_generated_array)) # Склеиваем С использованием np.vstack
print("\n" * 2, array_vstack.shape)
parts = np.vsplit(array_vstack, 10)  # Разделяем массив на 100 равных частей
all_parts = [] # Создаем список для хранения всех частей
for part in parts: # Сохраняем все части в цикле
    all_parts.append(part)
for i, part in enumerate(all_parts): # Выводим форму каждой части
    print(f"Форма части {i+1}: {part.shape}")



# np.hstack: Этот метод используется для горизонтальной стыковки массивов.
# Он объединяет массивы вдоль горизонтальной оси (по столбцам).
array_hstack = np.hstack((my_array, my_generated_array)) # Склеиваем С использованием np.hstack
print("\n" * 2, array_hstack.shape)
parts = np.hsplit(array_hstack, 10)  # Разделяем массив на 10 равных частей
for i, part in enumerate(parts):# Сохраняем каждую часть в отдельную переменную
    globals()[f"part{i+1}"] = part
for i, part in enumerate(parts): # Выводим форму каждой части
    print(f"Форма части {i+1}:", part.shape)

"""
Задача 3
Найдите все элементы массива my_array, которые больше трех и меньше 5 одновременно.
Используйте методологию подвыборки массива с условием (раздел "Индексация").
"""

condition = (my_array > 3) & (my_array < 5) # Создаем условие для элементов больше трех и меньше пяти
result = my_array[condition] # Используем условную индексацию для нахождения элементов, удовлетворяющих условию
print(result.shape)

"""
Задача 4
Создайте трехмерный массив размера 2 на 3 на 4,
состоящий из случайных ВЕЩЕСТВЕННЫХ чисел от 15 до 37.
Используйте встроенные методы библиотеки np.random.
"""

my_3d_array = np.random.uniform(15, 37, size=(2, 3, 4)) # Создаем трехмерный массив размера 2 на 3 на 4 из случайных вещественных чисел от 15 до 37
print(my_3d_array.shape)




"""
Задача 5
Используя массив из предыдущей задачи, преобразуйте его в новый массив со следующими значениями:

* "small", если значения меньше 20
* "medium", если значения в промежутке [20, 30]
* "large", если значения больше 30
Решение:
"""
conditions = [
    (my_3d_array < 20), # Если значение меньше 20, то соответствующий элемент в `conditions` становится True.
    (my_3d_array >= 20) & (my_3d_array <= 30), # Если значение находится в диапазоне от 20 до 30 включительно, то второй элемент в `conditions` становится True.
    (my_3d_array > 30) # Если значение больше 30, то третий элемент в `conditions` становится True.
]
choices = ['small', 'medium', 'large'] # создается список `choices` 'small' для значений меньше 20, 'medium' для значений от 20 до 30 и 'large' для значений больше 30.
new_array = np.select(conditions, choices) # используется для выбора соответствующего значения из `choices` для каждого элемента в `my_3d_array` в зависимости от соответствующего условия из `conditions`.
print(new_array)