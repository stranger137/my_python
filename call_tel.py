def mycall(city_code, time):
    if city_code == 343:
        price = 15
    elif city_code == 381:
        price = 18
    elif city_code == 473:
        price = 13
    elif city_code == 485:
        price = 11
    else:
        return "Unknown code"
    ans = price*time
    return ("The cost of your call is", ans, "roubles") #простите, я так и не нашла,как убрать запятые из вывода
        
print(mycall(343, 2))
print(mycall(0, 5))