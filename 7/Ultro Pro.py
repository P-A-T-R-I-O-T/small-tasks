import math



# Задача 1
#
# Уже весна, скоро в отпуск.
# Необходимо написать функцию расчета стоимости вашего путешествия.
#
# Определите функцию с названием hotel_cost и
# с аргументом "Количество ночей" в качестве входных данных.
# Цена отеля будет 140 у. е. за ночь.
# Выходит, функция должна вернуть стоимость всех ночей.
#
# Определите функцию под названием plane_ride_cost, \
# которая на вход принимает строку "Город".
# Такая функция должна вернуть цену перелета в зависимости от места:
# если это Крым, то перелет обойдется в 120 у. е.,
# если Шри-Ланка - 800 у. е., если Каир - 400 у. е., если Сочи - 120 у. е.
#
# Напишите функцию rental_car_cost с аргументом "Количество дней".
# Эта функция должна рассчитать стоимость аренды авто,
# если за сутки вы должны оплачивать саму ренту
# (40 у. е.) + стоимость услуг страхового агентства
# (+1% от суммарной стоимости услуг каждый следующий день.
# Т. е. первый день 1% от стоимости,
# второй - берется 1% от стоимости предыдущего дня
# (включая 1% за предыдущий день) и т. д.
# (следовательно сумма аренды авто за первый день будет составлять
# 40 * 1.01, за второй день 40 * 1.01 * 1.01,
# за третий день 40 * 1.01 * 1.01 * 1.01 и т.д.)
# Если вы арендуете на 7 и более дней,
# то скидка - 50 у. е., если от 3 до 6 дней включительно - 20 у. е.
# Обе скидки получить сразу нельзя.
# Задача состоит в том, чтобы эти функции
# (hotel_cost, plane_ride_cost, rental_car_cost)
# были локальными в составе одной глобальной функции trip_cost,
# которая бы возвращала сумму этих локальных функций.





def trip_cost(city, number_nights, number_days):
    def hotel_cost(number_nights): # Функция вычисляет сколько будет стоить сумма всех ночей в отеле
        price_hotel = 140 # фиксированная стоимость одной ночи в отеле
        return(number_nights * price_hotel)

    print("Стоимость гостиницы составит: ", hotel_cost(number_nights), "у.е.") # Вызываем функцию и выводим результат действия функции на экран


    def plane_ride_cost(city):
        if city == 'Крым':
            return 120
        elif city == 'Шри-Ланка':
            return 800
        elif city == 'Каир':
            return 400
        elif city == 'Сочи':
            return 120
    print("Стоимость перелёта в ", city, "составит ", plane_ride_cost(city), " у.е.")

    def rental_car_cost(number_days):
        daily_rent = 40
        insurance_rate = 1.01
        total_cost = 0

        for number_days in range(1, number_days + 1):
            total_cost += daily_rent * (insurance_rate ** (number_days - 1))

        if number_days >= 7:
            total_cost -= 50
        elif number_days >= 3:
            total_cost -= 20
        return total_cost
    print(f"Стоимость аренды автомобиля составит: {round(rental_car_cost(number_days), 2)} у.е.")
    return hotel_cost(number_nights) + plane_ride_cost(city) + rental_car_cost(number_days)

def choosing_place_relax():
    while True:
        print("Выбор места отдыха")
        print("1 Крым")
        print("2 Шри-Ланка")
        print("3 Каир")
        print("4 Сочи")
        choice = input('Выберите пункт место отдыха: ')
        if choice == '1':
            city = 'Крым'
            return city
        elif choice == '2':
            city = 'Шри-Ланка'
            return city
        elif choice == '3':
            city = 'Каир'
            return city
        elif choice == '4':
            city = 'Сочи'
            return city
        else:
            break
city = choosing_place_relax()
number_nights = int(input("Сколько ночей у вас будет? "))
number_days = int(input("Сколько дней будете арендовать машину? "))
print(f"Стоимость отдыха составит: {round(trip_cost(city, number_nights, number_days), 2)} у.е.")




# Задача 2
# Напишите функцию, которая считает факториал заданного числа.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = int(input("Введите число от которого нужно считать факториал: "))
print(factorial(n))


# Задача 3
# Напишите лямбда-функцию, которая считает полную площадь конуса: S = πR(l + R).

cone_surface_area = lambda R, l: math.pi * R * (l + R)

R = int(input("Введите радиус Конуса "))
l = int(input("Введите высоту Конуса "))
print(cone_surface_area(R, l))


# Задача 4
#
# Напишите 2 локальные функции,
# которые будут переводить рубли в доллары и рубли в евро,
# внутри глобальной функции,
# которая будет принимать на вход число (рубли)
# и выводить конвертированные валюты(доллары и евро).

def convert_currency(rubles):
    # Локальная функция для конвертации рублей в доллары
    def rubles_to_dollars(rubles):
        exchange_rate = 0.013  # примерный курс доллара к рублю
        return rubles * exchange_rate

    # Локальная функция для конвертации рублей в евро
    def rubles_to_euros(rubles):
        exchange_rate = 0.011  # примерный курс евро к рублю
        return rubles * exchange_rate

    # Вывод конвертированных валют
    print(f"{rubles} рублей равно {rubles_to_dollars(rubles)} долларов")
    print(f"{rubles} рублей равно {rubles_to_euros(rubles)} евро")

# Пример использования
convert_currency(1000)


# Задача 5
#
# Напишите функцию-генератор, которая будет выводить числа Фибоначчи.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования генератора
fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))


