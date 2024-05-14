import pandas as pd
"""
Pandas часть 1. Домашнее Задание. Light
Задача 1
Загрузите базу температур любым удобным способом.
Выведите базу. Посчитайте число пустых записей в столбце State.
Ссылка на скачивание базы: https://drive.google.com/file/d/1bLiz_81Kb4pMryEalRe66jS38_F6vwMX/view?usp=sharing
"""

df = pd.read_csv('city_temperature.csv', low_memory=False) # Записывает данные файла в переменную.
# Опция low_memory=False указывает на то, что pandas не должен использовать режим низкой памяти при загрузке данных
print(df)
empty_values_count = df['State'].isnull().sum() # Выбирает столбец State и
# применяет метод `isnull()`, который возвращает булеву серию, указывающую на пустые значения,
# и затем суммирует количество пустых значений в этом столбце
print('число пустых записей в столбце State: ', empty_values_count)

"""
Задача 2
Заполните пустые данные в базе словом "No". Запишите результат в ту же переменную. Выведите ее на экран.
"""
df = df.fillna('No') # заполняет все пустые значения DataFrame переменной '' строкой 'No'
print(df)

"""
Задание 3
При помощи метода Pandas определите число уникальных записей в столбцах Country, City, Year.
"""
unique_countries = df['Country'].nunique() # Метод nunique() возвращает количество уникальных значений в столбце Country
unique_cities = df['City'].nunique()
unique_years = df['Year'].nunique()
print(unique_countries)
print(unique_cities)
print(unique_years)

"""

Задача 4
При помощи библиотеки Pandas выведите строки, где в столбце Country встречается страна Russia.
При помощи метода Pandas отдельно выведите число элементов в этой выборке.
"""
russia_data = df[df['Country'] == 'Russia'] # В колонке Country выбираем записи только с Россией
print(russia_data)
russia_count = russia_data.shape[0] # Этот код вычисляет количество строк (зисей)
print("Количество элементов: ", russia_count)

"""
Задача 5
Создайте новый столбец температур, в котором будут записаны те же значения AvgTemperature, 
но в градусах Цельсия (исходная единица измерения - градусы Фаренгейта).
"""
df['Avg_Temp_Celsius'] = (df['AvgTemperature'] - 32) * 5/9
print(df)
