import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import pandas as pd



"""
Домашнее задание по Matplotlib и Seaborn
Light
Часть 1. Matplotlib
Задача 1
Используя библиотеку Matplotlib, постройте график экспоненты.
Подпишите оси. Дайте название графику.


import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
import pandas as pd 
/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
  import pandas.util.testing as tm
"""
x = np.linspace(0, 15, 100) # Задаём пространство точек, данные берём из любые
y = np.exp(x) # Функция экспоненты от оси (X)

# plt.plot(x, y) # Создание графика
# plt.title('график экспоненты') # Добавляем название графика
# plt.ylabel('Ось Y') # Подписываем ось
# plt.xlabel('Ось X') # Подписываем ось
# plt.grid() # Добавляем линии сетки
#
# plt.show()



"""
Задача 2
2 балла

Используя библиотеку Matplotlib, постройте графики функций y=x3 и y=x2 на одном графике.

Дайте название графику
Дайте названия осям
Присвойте лейблы и выведите легенду
Графики функций должны быть отрисованы пунктирными линиями (любыми из доступных на ваш вкус)
"""
y1 = x ** 3
y2 = x ** 2

# plt.plot(x, y1, linestyle = '--', label='x^3') # Создание графика? указываем стиль линии и подпись
# plt.plot(x, y2, linestyle = ':', label='x^2') # Создание графика? указываем стиль линии и подпись
# plt.title('графики функций y=x3 и y=x2') # Добавляем название графика
# plt.ylabel('Ось Y') # Подписываем ось
# plt.xlabel('Ось X') # Подписываем ось
# plt.grid() # Добавляем линии сетки
# plt.legend()
#
# plt.show()


"""
Задача 3
Выведите на экран картинку ascent, которая подгружается кодом ниже.

# Загружаем картинку из библиотеки scipy
from scipy import misc
img = misc.ascent()
"""

# img = misc.ascent() # Импортируем стандартную картинку
# plt.imshow(img)
# plt.show()


"""
Часть 2. Seaborn
Задача 4
Подгрузите данные datatraining.txt
при помощи соответствующей функции библиотеки Pandas.
Преобразуйте индекс в datetime index, удалите столбец с датой.
Постройте график всех парных взаимосвязей
с разметкой цвета в соответствии с метками классов (столбец Occupancy).

P.S. Используйте функцию sns.pairplot c параметром hue.

# Подгружаем google-диск
from google.colab import drive 
drive.mount('/content/drive/')
"""
df = pd.read_csv(os.path.join("baza", "datatraining.txt"))
# print(df)
df.index = pd.to_datetime(df['date']) # Преобразуем сталбец с индексами в столбец 'date'
# print(df)
df.drop('date', axis=1, inplace=True) # Удаляем столбец 'date', по счёту 1 (счёт начинается с 0)
sns.pairplot(data=df, hue='Occupancy')
plt.show()

"""
Задача 5
Постройте violinplot всех признаков датасета из прошлой задачи.
P.S. График должен быть читаемым. Для этого необходимо:
отрегулировать размер графика,
предварительно отскалировать все числовые признаки,
т. е. привести данные к стандартному нормальному распределению
при помощи питоновой функции scale, которая предоставляется ниже.
# Функция для скалирования
def scale(df):
    return (df - df.mean()) / df.std()
"""

def scale(df):
    return (df - df.mean()) / df.std()

df_scale = scale(df)
plt.figure(figsize=(15, 8)) # Меняем размер полотне

sns.violinplot(data=df_scale.drop('Occupancy', axis=1), orient='h')
plt.show()

