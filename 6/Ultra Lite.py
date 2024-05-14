import matplotlib.pyplot as plt
import seaborn as sns

"""
Добавить проект!!!!!! PyQt6 !!!!!!!
"""
"""
Домашнее задание по Matplotlib и Seaborn
Ultra light
Часть 1. Matplotlib
Импортируем библиотеки matplotlib и seaborn
Задача 1
На основе данных x и y, представленных ниже, постройте 2 графика plot(x,y) и scatter(x,y) на разных плоскостях.

# Данные для построения графика
x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]
"""
x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]
plt.plot(x, y)
plt.show()

plt.scatter(x,y)
plt.show()




"""
Задача 2
Добавьте на предыдущий график plot линии сетки,
подписи осей х и y, название графика "Самолет".
Сделайте размер графика (6, 3).
"""
plt.subplots(figsize=(6, 4)) # азмер графика (6, 3)
plt.plot(x, y)
plt.title('Самолёт') # Подписываем график
plt.xlabel('ОСЬ X') # Подписываем Ось Х
plt.ylabel('ОСЬ Y') # Подписываем Ось Y
plt.grid() # Добавляем линию сетки
plt.show()





"""
Задача 3
Постройте, на основе приведенного ниже словаря,
диаграмму. Ключи словаря будут подписями на оси х.

# Данные для построения диаграммы
data = {'Яблоки': 10, 'Апельсины': 15, 'Лимоны': 5, 'Лайм': 20}
names = list(data.keys())
values = list(data.values())
"""
data = {'Яблоки': 10, 'Апельсины': 15, 'Лимоны': 5, 'Лайм': 20}
names = list(data.keys())
values = list(data.values())

plt.bar(names, values) # Строим деаграмму
plt.show()


"""
Часть 2. Seaborn
Задача 4
Постройте boxplot на основе списка spis,
приведенного ниже. Измените цвет графика на зеленый.

# Список значений
spis = [2, 4, 1, 5, 6, 13]
"""
spis = [2, 4, 1, 5, 6, 13]
sns.boxplot(spis, color='g')
plt.show()


"""
Задача 5
Постройте график lmplot на основе датафрейма,
приведенного ниже (строить нужно по данным столбца 'x' и 'y').
Подгружаем датасет "anscombe"
df = sns.load_dataset("anscombe")
# Выводим первые 5 строк датасета
df.head(5)
"""

df = sns.load_dataset("anscombe")
# Выводим первые 5 строк датасета
print(df.head(5))

sns.lmplot(data=df, x='x', y='y')
plt.show()