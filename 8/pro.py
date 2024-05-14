import numpy as np

# Создание матрицы A и B размера 4x4 со случайными целыми числами от 1 до 10
A = np.random.randint(1, 11, size=(4, 4))
B = np.random.randint(1, 11, size=(4, 4))

# Создание вектора x размера 4 со случайными целыми числами от 1 до 5
x = np.random.randint(1, 6, size=(4, 1))

# Вычисление AA^T
A_transpose = A.T
AA_transpose = np.dot(A, A_transpose)

# Вычисление F(x) = 125 * AA^T * x + B * x + 5
F_x = 125 * np.dot(AA_transpose, x) + np.dot(B, x) + 5

print("Матрица A:\n", A)
print("Матрица B:\n", B)
print("Вектор x:\n", x)
print("Результат F(x):\n", F_x)



import matplotlib.pyplot as plt

# Функция
def f3(x):
    y = x*x*np.sin(x/300) + 300*x
    return y

# Диапазон значений x для построения графика
x_values = np.linspace(-1000, 1000, 10000)

# Вычисление значений функции f3(x)
y_values = f3(x_values)

# Поиск точек пересечения с осью X
zero_crossings = np.where(np.diff(np.sign(y_values)))
x_crossings = x_values[zero_crossings]

# Отображение функции
plt.plot(x_values, y_values)

# Отображение точек пересечения с осью X
plt.scatter(x_crossings, np.zeros_like(x_crossings), c='red', marker='o')

plt.xlabel('x')
plt.ylabel('f3(x)')
plt.title('График функции f3(x) с точками пересечения с осью X')
plt.grid(True)
plt.show()




def check_commutativity(matrix_a, matrix_b):
    return np.array_equal(np.dot(matrix_a, matrix_b), np.dot(matrix_b, matrix_a))

num_experiments = 1000
successful_count = 0

for _ in range(num_experiments):
    matrix_a = np.random.randint(-5, 6, size=(5, 5))
    matrix_b = np.random.randint(-5, 6, size=(5, 5))

    if check_commutativity(matrix_a, matrix_b):
        successful_count += 1

print("Количество успешных срабатываний:", successful_count)