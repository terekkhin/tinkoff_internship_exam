# task_6

# Однажды ковбой Джо забрёл в жуткую заброшенную шахту, в которой обитают n духов с номерами 1, 2, ..., n. Сейчас
# каждый дух состоит в банде из самого себя. В один момент времени каждый дух может находиться ровно в одной банде.
# По одиночке духи слабы, поэтому вскоре банды начнут объединяться. Когда две банды объединяются, создается новая банда,
# в которую попадают все духи из объединяющихся банд, в то время как старые банды распадаются.
# Ковбоя Джо оглушил душераздирающий крик, который сообщил ему о необходимости ответить на m вопросов. Если ковбой Джо
# откажется отвечать на вопросы крика или ошибется, то навечно сгинет в заброшенной шахте.
# Дух задаст m вопросов, каждый из которых относится к одному из трех типов.
# 1. Духи x и y объединяются в банду. Если они уже находятся в одной банде, ничего не происходит.
# 2. Крик спрашивает у ковбоя Джо, находятся ли духи x и y в одной банде.
# 3. Крик спрашивает ковбоя Джо, в скольких бандах побывал дух x.
#

n, m = map(int, input().split())
gangs = [set([i]) for i in range(n)]
num_of_gangs_been_in = [1] * n

for _ in range(m):
    curr_question = list(map(int, input().split()))
    curr_question[1] -= 1

    if curr_question[0] == 1:
        curr_question[2] -= 1
        if curr_question[1] not in gangs[curr_question[2]]:
            for ghost in gangs[curr_question[1]].copy():
                gangs[ghost].update(gangs[curr_question[2]])
            for ghost in gangs[curr_question[2]].copy():
                gangs[ghost].update(gangs[curr_question[1]])
            for ghost in gangs[curr_question[1]]:
                num_of_gangs_been_in[ghost] += 1
    elif curr_question[0] == 2:
        curr_question[2] -= 1
        if curr_question[1] in gangs[curr_question[2]]:
            print('YES')
        else:
            print('NO')
    elif curr_question[0] == 3:
        print(num_of_gangs_been_in[curr_question[1]])
