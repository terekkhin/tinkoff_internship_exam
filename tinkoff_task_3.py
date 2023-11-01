# task_3

# Перед ковбоем Джо выложены n карт со значениями a1, a2, ..., an. Он хочет получить выигрышную
# последовательность карт со значениями b1, b2, ..., bn.
# Ковбой может выбрать непрерывный отрезок карт в своей последовательности [l, r] (1 <= l <= r <= n)
# и упорядочить карты в этом отрезке по неубыванию. Например, если перед ковбоем лежат карты {3, 3, 2, 5, 1, 5},
# он может выбрать отрезок [2, 5] И получить последовательность {3, 1, 2, 3, 5, 5}.
# Получитсся ли у ковбоя Джо получить выигрышную последовательность с помощью применения
# вышеописанной операции ровно один раз?

def win_combination():
    n = int(input())
    joe_combination = list(map(int, input().split()))
    win_combination = list(map(int, input().split()))

    left = 0
    right = n

    for i in range(n):
        if joe_combination[i] != win_combination[i]:
            left = i
            break

    for i in range(left + 1, n):
        if win_combination[i - 1] > win_combination[i]:
            right = i
            break

    joe_combination = joe_combination[:left] + sorted(joe_combination[left:right]) + joe_combination[right:]

    if joe_combination == win_combination:
        return 'YES'
    return 'NO'


print(win_combination())