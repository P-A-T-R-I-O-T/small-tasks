import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import pandas as pd

"""
Ultra Pro
Часть 1. Matplotlib
Задача 1
Подгрузите любую картинку любым способом и выведите её на экран.
Измените её размер на 480х320,
добавьте зеленый прямоугольник в любом месте экрана и выведите результат.

from google.colab import drive # Подключаем гугл-диск
drive.mount('/content/drive')

from PIL import Image, ImageDraw # Модули работы с изображениями
"""
from PIL import Image, ImageDraw # Модули работы с изображениями
image = Image.open(os.path.join("baza", "face-galaxy-planet.jpg")) # открываем картинку
plt.imshow(image) # Создаём область отображения и помещяем туда нашу картинку
plt.show() # Выводим на экран

image = image.resize((480, 320)) # Меняем размер
img = ImageDraw.Draw(image) # Создаём экземпляр изображения
img.rectangle([100, 150, 200, 300], outline='green', width=5) # Добавляем зелёный прямоугольник
plt.imshow(image) # Создаём область отображения и помещяем туда нашу картинку
plt.show() # Выводим на экран

"""
Задача 2
На основе данных, приведенных ниже,
постройте парную гистограмму как на рисунке
(100% сходство не обязательно). image.png

labels = ['группа 1', 'группа 2', 'группа 3', 'группа 4', 'группа 5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
"""
labels = ['группа 1', 'группа 2', 'группа 3', 'группа 4', 'группа 5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels)) # Значение для оси X
width = 0.35 # задаём ширину стольбиков диаграммы
fig, ax = plt.subplots() # Создаём фгуру
# Строим 2 диаграммы, мужцин и женщин
rects1 = ax.bar(x - width/1.9, men_means, width, label='Мужчины')
rects2 = ax.bar(x + width/1.9, women_means, width, label='Женьщины')
# Указываем название графика и подписываем оси
ax.set_ylabel('Количество')
ax.set_title('Количество людей в группах с разбивкой по полу')
ax.set_xticks(x)

ax.set_xticklabels(labels)
ax.legend()
plt.show()


"""
Часть 2. Seaborn
Задача 3
Используя датасет "Ирисы", подгруженный кодом ниже,
постройте график всех парных взаимосвязей с разметкой цвета
в соответствии с метками классов (столбец species).

iris = sns.load_dataset("iris")
iris
"""
iris = sns.load_dataset("iris")
print(iris)
print(iris["species"].unique()) # Смотрим наименование значений в данном столбце, данного датафрейма
sns.pairplot(iris, hue="species") # Строим график pairplot, hue="species" разбивка по цветам
plt.show()




"""
Задача 4
Используя датасет ниже "flights",
посчитайте сумму ежегодных перелетов пассажиров
(используя преобразование столбца "year" в столбец временных индексов)
и постройте диаграмму, отображающую количество пассажиров за каждый год.

df = sns.load_dataset("flights")
df
"""
df = sns.load_dataset("flights")
df.index = pd.to_datetime(df.year, format= '%Y') # Преобразуем индыксы в формат DateTime Index
df.drop(columns="year", inplace=True) # Удаляем столбец "year" так как он уже преобразован в индексы
df['passengers'] = pd.to_numeric(df['passengers'], errors='coerce')
df['passengers'] = df['passengers'].astype(float)  # Преобразование в тип данных float
df_grouped = df.groupby('year')[['passengers']].sum()  # Выполнение группировки и суммирования по годам
# Построение графика
plt.figure(figsize=(12, 6))
df_grouped.index = df_grouped.index.strftime('%Y')
print(df_grouped.index)
sns.barplot(x=df_grouped.index, y='passengers', data=df_grouped)
plt.xlabel('Года')
plt.ylabel('Всего пассажиров')
plt.title('количество пассажиров за каждый год')
plt.show()

"""
Задача 5
Используя датасет "flights" из предыдущей задачи,
постройте 12 boxplot'ов для каждого месяца на одном графике.
Приведите в порядок размер и тики, чтобы график был читаемым.
"""

df = sns.load_dataset("flights")

plt.figure(figsize=(12, 6))
sns.boxplot(data=df.drop(columns='year'), x='month', y='passengers')
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('Boxplot для количества пассажиров по месяцам')
plt.xticks(ticks=range(0, 12), labels=['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'])
# plt.xticks(rotation=90)
plt.show()