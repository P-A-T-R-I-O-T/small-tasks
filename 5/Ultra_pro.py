import pandas as pd
import os

"""
Pandas часть 2. Домашнее Задание. Ultra-Pro
Задача 1
Подгрузите данные 'data.csv' (возможно, придется указать кодировку encoding сp1250) в переменную data.
Создайте новый столбец TotalCost со значениями Quantity * UnitPrice.
Сделайте resampling данных в еженедельные со значениями суммы по столбцам TotalCost.
"""
data = pd.read_csv(os.path.join("baza", "data.csv"), encoding='cp1250')

data['TotalCost'] = data.Quantity * data.UnitPrice
data.index = pd.to_datetime(data['InvoiceDate']) # Преобразуем колонку InvoiceDate к типу datetime
data_resampling = data.resample('W').sum()
# print(data_resampling['TotalCost'])
"""
Задача 2
Посчитайте скользящее недельное среднее суммы ежедневных заказов. Для этого

сделайте resampling в ежедневные данные,
посчитайте скользящее среднее за 7 дней по столбцу TotalCost.
Для решения второй части данной задачи потребуется самостоятельно найти способ определения скользящего среднего.
"""
# print(data.TotalCost.resample('d').sum().rolling('7d').mean())

"""
Задача 3. GroupBy
Посчитайте общую стоимость заказов на ежемесячной основе в разбивке по странам.
"""
data2 = data.groupby(['Country']).TotalCost.resample('ME').sum()
# print(data2.head(20))

"""

Задача 4. JOIN
Подгрузите данные, содержащие информацию о номерах карт лояльности пользователей (card_data.csv).
Назовите ее cards.
Сделайте Left Join исходной таблицы (которая получилась после задачи с datetime индексом) и таблицы cards.
Если будет переполнение памяти, попробуйте взять не все значения таблицы, а, например, первые 100 с помощью соответствующего метода iloc.
"""
data = pd.read_csv(os.path.join("baza", "data.csv"), encoding='cp1250')
data.drop('InvoiceDate', axis=1, inplace=True)
data = data[::100]

cards = pd.read_csv(os.path.join("baza", "card_data.csv"), encoding='cp1250')
cards = cards[::100]

data2 = data.merge(cards, how='left', on='CustomerID')
print(data2.columns)


"""
Задача 5
Выведите квантили 0.4 и 0.6 по численным данным новой таблицы там, где это имеет смысл.
"""
print(data2[['UnitPrice', 'TransactionNum', 'Quantity']].quantile([0.4, 0.6]))