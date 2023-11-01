# task_1

# Однажды ковбой Джо решил обзавестись револьвером и пошел в оружейный магазин. У ковбоя s
# долларов, а на выбор представлены n револьверов с ценами a1, a2, ..., an.
# Помогите ковбою Джо выбрать самый дорогой револьвер, который он может себе позволить или
# сообщите, что такого не существует

def price():
    n, s = map(int, input().split())

    weapon_prices = list(map(int, input().split()))
    weapon_prices.sort(reverse=True)

    for i in weapon_prices:
        if i <= s:
            return i
    return 0

print(price())