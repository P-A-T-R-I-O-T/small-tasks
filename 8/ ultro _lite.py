import numpy as np

# Создаем скаляр
scalar = np.array(5)
print("Скаляр:")
print(scalar)
print("Форма: ", scalar.shape)
print("Число элементов: ", scalar.size)

# Создаем вектор размера 5
vector = np.array([1, 2, 3, 4, 5])
print("\nВектор размера 5:")
print(vector)
print("Форма: ", vector.shape)
print("Число элементов: ", vector.size)

# Создаем матрицу размера 5x5
matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
print("\nМатрица размера 5x5:")
print(matrix)
print("Форма: ", matrix.shape)
print("Число элементов: ", matrix.size)


# Сложение скаляра с вектором
added_scalar_vector = scalar + vector
print("Сумма скаляра и вектора:\n", added_scalar_vector)

# Умножение скаляра на вектор
multiplied_scalar_vector = scalar * vector
print("Произведение скаляра и вектора:\n", multiplied_scalar_vector)

# Деление матрицы на скаляр
divided_matrix_scalar = matrix / scalar
print("Матрица, разделенная на скаляр:\n", divided_matrix_scalar)

# Сложение матрицы со скаляром
added_matrix_scalar = matrix + scalar
print("Матрица, добавленная к скаляру:\n", added_matrix_scalar)

# Сложение матрицы с вектором
added_matrix_vector = np.add(matrix, vector)
print("Сумма матрицы и вектора:\n", added_matrix_vector)




# Транспонирование матрицы
transposed_matrix = np.transpose(matrix)
print("Транспонированная матрица:\n", transposed_matrix)

# Вычисление обратной матрицы
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Обратная матрица:\n", inverse_matrix)
except np.linalg.LinAlgError:
    print("Матрица является вырожденной, обратная матрица не может быть вычислена")

# Матричное умножение самой на себя
matrix_squared = np.dot(matrix, matrix)
print("Матричное умножение самой на себя:\n", matrix_squared)




# Создание массива из 1000 целых значений от 0 до 1000 не включительно
axis_x = np.arange(0, 1000, 1)

# Вывод массива на экран
print(axis_x)

#В результате Вы получите вектор (одномерный массив) из 1000 целых чисел.