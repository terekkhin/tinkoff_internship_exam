# task_5

# Древний индейский дух Чогэн пробудился и отправился карать бледнолицых. Ничто не способно его остановить,
# так что ковбой Джо выступает в роли наблюдателя в этой задаче.
# На Диком западе n городов и m двусторонних лорог между ними. Штатом называется такое множество городов, для которого верно:
# 1. Из любого города множества можно добраться по дорогам до любого другого города из этого множества;
# 2. Из любого города этого множества нельзя добраться по дорогам до любого города не из этого множества;
# Из любого города можно добраться по дорогам до самого себя, используя 0 дорог
# Дух Чогэн выбирает целое число x и уничтожает все дороги длиной не более x. Несложно заметить,
# что Дикий запад однозначно разбивается на штаты. Дух Чогэн хочет уничтожить как можно больше дорог,
# но количество штатов должно остаться неизменным. Помогите духу найти число X.

def find_number_of_components(graph):
    v = len(graph)
    visited = [False] * v
    answer = 0

    for i in range(v):
        if visited[i]:
            continue
        answer += 1
        visited[i] = True
        queue = [i]
        while queue:
            curr_v = queue.pop()
            for to in graph[curr_v]:
                if not visited[to]:
                    visited[to] = True
                    queue.append(to)
    return answer


def create_graph(data, v):
    if len(data) == 1:
        return [[1], [0]]
    graph = [[] for _ in range(v)]
    for i in data:
        v_1, v_2 = i[0], i[1]
        graph[v_1].append(v_2)
        graph[v_2].append(v_1)
    return graph


def find_x():
    v, e = map(int, input().split())
    data = []

    for i in range(e):
        data.append([int(k) - 1 for k in input().split()])
        data[i][2] += 1

    graph = create_graph(data, v)
    number_of_components = find_number_of_components(graph)
    weights = sorted([i[2] for i in data])
    x = weights[0] - 1

    for i in weights:
        new_data = []
        for r in data:
            if r[2] > i:
                new_data.append(r)
        new_graph = create_graph(new_data, v)
        if number_of_components != find_number_of_components(new_graph):
            x = i - 1
            break
    return x


print(find_x())