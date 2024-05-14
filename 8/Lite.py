import numpy as np

def multiply_matrices(A, B, C):
    # Проверяем размеры матриц
    if A.shape[1] != B.shape[0] or B.shape[1] != C.shape[0]:
        raise ValueError("Нево умножить матрицы с данными размерами")
    
    # Инициализируем результирующую матрицу
    result = np.zeros((A.shape[0], C.shape[1]))
    
    # Выполняем умножение матриц
    for i in range(A.shape[0]):
        for j in range(C.shape[1]):
            for k in range(B.shape[1]):
                result[i, j] += A[i, k] * B[k, j] * C[j, k]
    
    return result

# Пример использования функции
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])

result = multiply_matrices(A, B, C)
print("Результат умножения трех матриц:\n", result)


def calculate_difference_max_min(matrix):
    # Проверка, является ли входной аргумент матрицей
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError("Входной аргумент должен быть матрицей (двумерным массивом)")

    # Нахождение максимального и минимального элементов матрицы
    max_value = np.max(matrix)
    min_value = np.min(matrix)

    # Расчет разницы между максимальным и минимальным элементами
    difference = max_value - min_value

    return difference

# Пример использования функции
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(calculate_difference_max_min(matrix))  # Вывод: 8



def multiply_and_invert(matrix):
    # Транспонирование матрицы
    transposed_matrix = np.transpose(matrix)
    
    # Умножение матрицы на транспонированную матрицу
    result_matrix = np.dot(matrix, transposed_matrix)
    
    # Получение обратной матрицы от результата
    try:
        inverse_result_matrix = np.linalg.inv(result_matrix)
        return inverse_result_matrix
    except np.linalg.LinAlgError:
        print("Ошибка: Вырожденная матрица, невозможно найти обратную.")
        return None

# Пример использования функции
inverse_matrix = multiply_and_invert(matrix)
print("Обратная матрица:", inverse_matrix)




import matplotlib.pyplot as plt


def function(x):
    return x**3/12 + x*(x-15) - 72

x = np.linspace(-10, 10, 1000)
y = function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = x^3/12 + x*(x-15) - 72')
#plt.grid()
#plt.show()



def func(x):
    return (x**3/12) + x*(x-15) - 72

x = np.arange(-10, 10.1, 0.1)
y = func(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = x^3/12 + x*(x-15) - 72 ////2')
plt.grid(True)
plt.show()