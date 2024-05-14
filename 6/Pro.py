import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
from sklearn import datasets
""" устанавливать библиотеку sklearn нужно использовать её scikit-learn"""

"""
Домашнее задание по Matplotlib и Seaborn
Pro
Часть 1. Matplotlib
Задача 1
Используя библиотеку Matplotlib, для датасета "Ирисы",
который подгружается кодом ниже,
нарисуйте точечную диаграмму (scatter plot) всех четырех признаков.
Каждый признак должен быть нарисован на отдельном графике.
Используйте для этого subplot формата 2 на 2.
Графики должны быть читаемыми, т. е. отрегулируйте размер subplot'ов.
Добавьте названия признаков к каждому графику в качестве имени графика
(названия признаков можно получить с помощью метода .feature_names).
Используйте метки классов (y) в качестве цветовой разметки.
Добавьте расшифровку цветов, соответствующих меткам классов, в качестве лейблов.
P.S. Используйте функцию plt.scatter(x, y, color).
from sklearn import datasets
data = datasets.load_iris(return_X_y=False)
X = data.data
y = data.target
names = data.target_names
"""


data = datasets.load_iris(return_X_y=False)
X = data.data
y = data.target
names = data.target_names


my_feature_names = data.feature_names # Записываем в переменную название призноков

plt.figure(1, figsize=(10,10)) # Создаём один большой график с размерностью 10х10
for i in range(4): # Создали цикл, который будет размещать данные на четырёх графиках
    l = 1
    plt.subplot(2,2, i+1) # Дём разметку нашего большого рафика на 2 столбца и 2 строки, задаём номирацию не с 0, а с 1
    plt.title(my_feature_names[i]) # Делаем подпись к нишим маленьким графикам
    plt.scatter(range(50), X[:50, i], label=names[0], c='r') # Строим точки внутри графика, по оси Х и y деляя их по 50 друк от друга назначаем первые 50 значений, параметр label подписывает точки согласно описанию, указываем цвет
    plt.scatter(range(50, 100), X[50:100, i], label=names[0], c='b') # Строим точки внутри графика, по оси Х и y деляя их по 50 друк от друга назначаем вторые 50 значений (от 50 до 100), параметр label подписывает точки согласно описанию, указываем цвет
    plt.scatter(range(100, 150), X[100:150, i], label=names[0], c='g') # Строим точки внутри графика, по оси Х и y деляя их по 50 друк от друга назначаем третьи 50 значений (от 100 до 150), параметр label подписывает точки согласно описанию, указываем цвет
    plt.xlabel('index') # подписи осей X
    plt.ylabel(my_feature_names[i]) # подпись осей Y
    plt.legend() # Выводим легенду (подпись внутри самих графиков)
plt.show()


"""
Задача 2
Используя библиотеку Matplotlib,
постройте гистограмму для первого признака в датасете выше следующим образом:

на одном графике должно быть три гистограммы, по одной на каждый класс,
для этого используйте методологии подвыборки массива с условием,
количество бинов должно определяться автоматически (режим "auto"),
гистограмма должна быть читаемой, т. е. добавьте подписи, лейблы, названия и т. д.
"""

plt.hist(X[:50,0]) # выкодим первые 50 значений Х
plt.hist(X[50:100 ,0], alpha=0.7) # Добавляем следующие 50 значений и делаем прозрачность 0,7
plt.hist(X[100:, 0], alpha=0.7) # Добавляем остальные значения по Х
plt.title('Гистограмма первого признака') # Делаем название графика
plt.xlabel(my_feature_names[0]) # Подпись по оси Х
plt.ylabel('Количество экземпляров') # Подпись по оси Y
plt.legend(names) # Выводим легенду внутри графика
plt.show()

"""
Задача 3

Используя библиотеку Matplotlib,
посчитайте матрицу корреляции между признаками и нарисуйте ее как heatmap.
Подберите подходящую по смыслу цветовую гамму.
Добавьте названия признаков в качестве тиков по осям.
Добавьте отрисовку цветовой шкалы.
"""
iris = pd.DataFrame(X, y) # Создаём датафрейм из значений X и Y
to_plot = iris.corr() # Считаем матрицу кореации, метадом corr
plt.imshow(to_plot, cmap='Blues') # Строим график с кориляцией и выстовляем оттенок синего Blues
plt.colorbar() # Выводим шкалу от чисто белого, до тёмно-синего
plt.xticks(range(4), my_feature_names, rotation=45, color='black') # Подписываем ось X, названием от my_feature_names, поворачиваем на 45 градусов и задаём цвет чёрный
plt.show()



"""
Часть 2. Seaborn
Задача 4
для датасета Occupancy (datatraining.txt)
постройте диаграмму присутствия в разбивке по часам и меткам классов
(метки классов хранятся в столбце 'occupancy)'.
Для этого сделайте следующее:

создайте новый столбец "hour", отвечающий соответствующему часу,
нарисуйте sns.countplot этого столбца в разбивке по Occupancy.
[ ]
from google.colab import drive 
drive.mount('/content/drive/')
Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3aietf%3awg%3aoauth%3a2.0%3aoob&scope=email%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdocs.test%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive.photos.readonly%20https%3a%2f%2fwww.googleapis.com%2fauth%2fpeopleapi.readonly&response_type=code

Enter your authorization code:
··········
Mounted at /content/drive/
"""
df = pd.read_csv(os.path.join("baza", "datatraining.txt"))
# print(df)
df.index = pd.to_datetime(df['date']) # Преобразуем сталбец с индексами в столбец 'date'
# print(df)
df.drop('date', axis=1, inplace=True) # Удаляем столбец 'date', по счёту 1 (счёт начинается с 0)
df['hour'] = df.index.hour # Создаём новый сталбец и значение разбиваем по чисавым значениям
# print(df)
sns.countplot(data=df, x=df.hour, hue='Occupancy')
plt.show()


"""
Задача 5
Сделайте resample данных по получасовому интервалу
с использованием усреднения для всех признаков.

Постройте sns.jointplot между признаками Light и CO2.
"""

fr1 = df.Occupancy.resample('30min').bfill() # Разбиваем на интервалы по 30 минут, метадом dfill
fr2 = df.iloc[:, :-1].resample('30min').mean() # Используем усреднение для основного датафрейма
res_fr = pd.concat([fr1, fr2]) # Соединяем данные в одну таблицу
sns.jointplot(x=res_fr.Light, y=res_fr.CO2, data=res_fr) # Создаём график с параметрами X и Y
plt.show()