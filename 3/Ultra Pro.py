import numpy as np

"""
Домашнее Задание. Ultra-Pro

Создайте единичную матрицу размером 5*5.
Должна получиться матрица вида

1 0 0 0 0

0 1 0 0 0

0 0 1 0 0

0 0 0 1 0

0 0 0 0 1

Действовать можно двумя путями:

Используя соответствующий метод Numpy. (О нем не говорилось в занятии. Стоит обратиться к документации Numpy).
Если первый вариант сложный, можно создать массив из нулей, используя метод, о котором говорилось в занятии. В цикле заменить все элементы по диагонали на единицы.
"""
# Этот код создает единичную матрицу размером 5x5 с использованием метода `np.eye` из библиотеки NumPy.
# Единичная матрица - это квадратная матрица,
# у которой все элементы равны нулю,
# за исключением элементов на главной диагонали, которые равны единице.
# В данном случае, матрица будет иметь вид:
# identity_matrix1 = np.eye(5)
# print(identity_matrix1)
#
#
# zero_matrix = np.zeros((5, 5)) # Создается матрица из нулей размером 5x5
# for i in range(5): # Затем запускается цикл `for i in range(5)`, который проходит по индексам от 0 до 4
#     zero_matrix[i, i] = 1 # На каждой итерации цикла элемент матрицы с координатами `[i, i]` (элементы по главной диагонали) устанавливается равным 1
# print(zero_matrix) # После прохода цикла выводится полученная матрица, в которой на главной диагонали стоят единицы


"""
Задача 2
Создайте массив из случайных значений из стандартного нормального распределения размера 6 на 6.
Разверните массив таким образом, чтобы его размер стал 36 на 1. Найдите среднее значение элементов массива.
Разрешается использовать только методы Numpy. (Циклы и условия запрещены).
"""
# my_array = np.random.randn(6, 6) # Создание массива из случайных значений стандартного нормального распределения
# # print(my_array)
# flattened_array = my_array.flatten() # Развернуть массив в одномерный массив
# # print(flattened_array)
# mean_value = np.mean(flattened_array) # Найти среднее значение элементов массива
# print("Среднее значение элементов массива:", mean_value)


"""
Задача 3
Создайте массив из 20 любых случайных значений, используя метод Numpy.
Найдите значения производных для созданного массива
"""

# my_array = np.random.rand(20) # Создаем массив из 20 случайных значений
# print(my_array)
# derivatives = np.gradient(my_array) # Находим значения производных
# print(derivatives)

"""
Задача 4
Дано выражение
Y = A * X * C
Создайте три случайных массива A, C, X.
Размерности должны позволять выполнить матричное умножение согласно формуле.
На выходе должен получиться массив Y с размерностью (5, 18).
(Остальные размерности возьмите на свое усмотрение).
"""
# Для создания случайных массивов A, C, X
# с подходящими размерностями для матричного умножения
# по формуле Y = A * X * C
# и получения массива Y размерностью (5, 18), можно сделать следующее:

# Создаем случайные массивы A, C, X с подходящими размерностями
# A = np.random.rand(5, 3)
# X = np.random.rand(3, 6)
# C = np.random.rand(6, 18)
#
# # Вычисляем массив Y по формуле Y = A * X * C
# Y = np.dot(np.dot(A, X), C)
# print(Y.shape)  # Размерность массива Y должна быть (5, 18)



"""
Задача 5
Загрузите какой-либо файл с данными
(таблица Excel с Вашего компьютера, сохраненная в формате csv, или таблица из Интернета).
Выведите следующее:

Всю информацию из файла в ячейку.
Размерность данных.
Среднее арифметическое от всех числовых значений (если есть).
Число столбов.
Число строк.
Типы данных всех значений.
"""
my_array = np.loadtxt('frez.csv', delimiter=',', skiprows=1, encoding='utf-16', dtype=str)
my_array_shape = my_array.shape
data_type = my_array.dtype
num_columns = my_array.shape[1]
num_rows = my_array.shape[0]

my_array = np.array([1, 2.5, 'hello', True])
for value in my_array:
    type(value)

info_my_array = {
    'shape' : my_array_shape,
    'data_type': data_type,
    'num_columns': num_columns,
    'num_rows': num_rows,
    'values_types': [type(value) for value in my_array]
}
print(info_my_array)