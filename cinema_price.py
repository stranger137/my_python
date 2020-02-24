print("Вас приветствует программа подсчета стоимости фильма. Пожалуйста, введите название:")
film_name = input()
film_time = 0
ticket_price = 0
sale = 0

if film_name == "1917":
    print("Выберите время сеанса: 10, 13 или 16 часов")
    film_time = int(input())
    if film_time == 10:
        ticket_price = 250
    else:
        ticket_price = 350
elif film_name == "Паразиты":
    print("Выберите время сеанса: 12, 16 или 20 часов")
    if film_time == 12:
        ticket_price = 250
    elif ticket_price == 16:
        ticket_price = 350
    elif ticket_price == 16 or ticket_price == 20:
        ticket_price = 450
    else:
        print("Введено неверное время. Повторите попытку")
elif film_name == "Соник в кино":
    print("Выберите время сеанса: 10, 14 или 18 часов")
    if film_time == 10:
        ticket_price = 350
    elif film_time == 14 or film_time == 18:
        ticket_price = 450
    else:
        print("Введено неверное время. Повторите попытку")
else:
    print("Введено неверное время фильма. Повторите попытку")
    
print("Когда Вы собираетесь посетить кино? Нажмите 0, если сегодня, 1 если завтра,на остальные даты нажмите любое другое число. Если Вы придете завтра, то Вас ждет скидка 5%!")
date = int(input())
if date == 1:
    sale += 5
print("Сколько суммарно человек придет вместе с Вами? Если больше 20, Вас ждет скидка 20%!")
people = int(input())
if people >= 20:
    sale += 20
    
ans = ticket_price*people*sale/100
print("Суммарная стоимость билетов", ans, "рублей. Приятного просмотра!")
