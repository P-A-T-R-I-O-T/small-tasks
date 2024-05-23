import pandas as pd
import os


"""
Pandas часть 2. Домашнее Задание. Pro
Задача 1. DateTime index
Подгрузите данные 'data.csv' (возможно, придется указать кодировку encoding cp1250) в переменную data.
Преобразуйте колонку InvoiceDate в DateTime index.
Удалите колонку InvoiceDate.
"""
data = pd.read_csv(os.path.join("baza", "data.csv"), encoding='cp1250')
data.index = pd.to_datetime(data.InvoiceDate)
# print(data.head())
data.drop('InvoiceDate', axis=1, inplace=True)
# print(data.head())


"""
Задача 2
Используя датафрейм data,
выберите все заказы,
совершенные за период 7 декабря 2010 года с часа дня до часа и одной минуты.
"""
# print(data['2010-12-07 13:00:00':'2010-12-07 13:01:00'])



"""
Задача 3
По той же рабочей табличке
посчитайте количество уникальных наименований товаров (Description),
которые купили за весь период (т. е. по всем данным).
Используйте соответствующий метод.
найдите все уникальные страны,
в которых были размещены заказы.
"""
# print(data.Description.nunique(), 'Количество уникальных товаров')
# print('Все страны', data.Country.unique().tolist())



"""
Задача 4
Посчитайте матрицу корреляции Спирмена для наших данных.
Найдите 1%, 50% и 99% квантили цены за единицу товара.
Для решения данной задачи потребуется самостоятельно найти способ
получения матрицы Спирмена.
Обратите внимание, на вебинаре продемонстрирован пример матрицы Пирсона.
"""
print(data.columns)
# print(data.dtypes)
col = ['Quantity', 'UnitPrice', 'CustomerID']
print(data[col].corr(method='spearman'))
print(data[col].quantile([0.01, 0.5, 0.99]))


"""
Задача 5
Найдите количество клиентов, которые оформляли заказ в понедельники. Для этого
сделайте подвыборку, соответствующую условию "в понедельник",
посчитайте количество уникальных ID клиентов.
Для решения этой задачи потребуется использовать параметр индекса weekday
(по аналогии с рассмотренными на вебинаре примерами .index.month, .index.day).
"""


print(data.CustomerID[data.index.weekday == 0].nunique())
# Считаем уникальных пользователей nunique() сделавших заказ в понедельник weekday == 0
