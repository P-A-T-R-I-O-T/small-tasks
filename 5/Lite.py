import pandas as pd
import os

"""
Pandas часть 2. Домашнее Задание. Light
1 бонусный балл, если все задачи покрыты комментариями,
которые описывают тактику решение задачи (до 10 баллов)
Задача 1
Загрузите базу статистики по приложениям из Google Play. 
Определите уникальные категории приложений. 
В цикле найдите число приложений по каждой категории.
Описание базы:
App - имя приложения
Category - категория
Rating - рейтинг
Reviews - число комментариев
Size - размер
Instals - число установок
Type - платное или бесплатное приложение
Content Rating - ограничения по возрасту
Genres - жанры
Last Updated - последнее обновление
Current Ver - текущая версия
Android Ver - версия для Android
Ссылка на базу: https://drive.google.com/file/d/1dwFUK1PxzVLSyzHjPImCw_XvTIP-llJQ/view?usp=sharing
"""
df = pd.read_csv(os.path.join("baza", "googleplaystore.csv"), low_memory=False)
# print(df)
category = df.Category.unique().tolist()
# print(category)
# for i in category:
#     print(i, ' ' * (8 -len(i)),df[df.Category == i].shape[0])



"""
Задача 2
Отсортируйте приложения по рейтингу при помощи встроенных методов Pandas.
"""
df_sorted = df.sort_values('Rating', ascending=False)
# print(df_sorted)


"""
Задача 3
Оставьте в выборке только те приложения,
которые имеют рейтинг в пределах от 5 до 3 (оба значения включительно).
Узнайте число платных и бесплатных приложений в этом списке при помощи методов Pandas.
"""
df_sorted2 = df_sorted[(df_sorted.Rating >= 3) & (df_sorted.Rating <= 5)]
print(df_sorted2)
print('Бесплатные', df_sorted2[df_sorted2.Type == 'Free'].shape[0])
print('Платные', df_sorted2[df_sorted2.Type == 'Paid'].shape[0])

"""
Задача 4
Обновите индексовый столбец датафрема,
что бы индексовый столбец заполнился новыми числами (любыми).
"""
df_sorted2.index = [i for i in range(df_sorted2.shape[0])]
print(round(df.isna().sum().sum() * 100 / df.size, 2), "%" )



"""
Задача 5
2 балла

Определите процент пустых ячеек к заполненным в начальной таблице. Результат выведите в процентах с округлением до двух знаков.
"""