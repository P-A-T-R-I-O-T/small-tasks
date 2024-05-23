"""Напишите функцию, которая находит две точки: где наклон графика функции самый крутой (в любую сторону), где наклон самый пологий, и отображает на графике функции эти точки зелёным и красным кругом соответственно.
"""


"""
Задача 2
Напишите функцию, которая находит все экстремумы двумерной функции z = sin(x) * sin(y) в диапазоне [x = -3.14, x = 3.14], [y = -3.14, y = 3.14], а также:

a) Возвращает листы с координатами двумерных точек - 4 листа - локальный и глобальный минимум и максимум.

b) Выводит график такой функции.
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def find_extremums(func, x_range, y_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    extremums = {
        'min': {'local': [], 'global': []},
        'max': {'local': [], 'global': []}
    }

    # Находим локальные минимумы и максимумы
    for i in range(1, len(x) - 1):
        for j in range(1, len(y) - 1):
            if (i > 0 and i < len(x) - 1 and j > 0 and j < len(y) - 1 and
                Z[i, j] < Z[i - 1, j] and Z[i, j] < Z[i + 1, j] and
                Z[i, j] < Z[i, j - 1] and Z[i, j] < Z[i, j + 1]):
                extremums['min']['local'].append((x[i], y[j], Z[i, j]))
            if (i > 0 and i < len(x) - 1 and j > 0 and j < len(y) - 1 and
                Z[i, j] > Z[i - 1, j] and Z[i, j] > Z[i + 1, j] and
                Z[i, j] > Z[i, j - 1] and Z[i, j] > Z[i, j + 1]):
                extremums['max']['local'].append((x[i], y[j], Z[i, j]))

    # Находим глобальные минимумы и максимумы
    extremums['min']['global'] = [min(extremums['min']['local'], key=lambda x: x[2])]
    extremums['max']['global'] = [max(extremums['max']['local'], key=lambda x: x[2])]

    return extremums

def plot_function(func, x_range, y_range, extremums):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    for extremum in extremums['min']['local']:
        ax.scatter(extremum[0], extremum[1], extremum[2], color='green')
    for extremum in extremums['max']['local']:
        ax.scatter(extremum[0], extremum[1], extremum[2], color='red')
    for extremum in extremums['min']['global']:
        ax.scatter(extremum[0], extremum[1], extremum[2], color='lime')
    for extremum in extremums['max']['global']:
        ax.scatter(extremum[0], extremum[1], extremum[2], color='crimson')

    plt.show()

# Функция, для которой ищем экстремумы
def func(x, y):
    return np.sin(x) * np.sin(y)

# Находим экстремумы
extremums = find_extremums(func, [-3.14, 3.14], [-3.14, 3.14])

# Выводим график функции с отмеченными экстремумами
plot_function(func, [-3.14, 3.14], [-3.14, 3.14], extremums)