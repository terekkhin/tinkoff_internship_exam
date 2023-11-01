# task_2

# Однажды ковбой Джо нанялся в помошники шерифу. Шериф выдал ковбою Джо строку s и попросил
# собрать из её букв как можно больше слов sheriff. Каждая буква можт использоваться не более чем в одном слове.

def sheriff():
    start_str = input()
    sheriff_dict = {'s': 0, 'h': 0, 'e': 0, 'r': 0, 'i': 0, 'f': 0}

    for i in start_str:
        if i in sheriff_dict:
            sheriff_dict[i] += 1

    return min(sheriff_dict['s'], sheriff_dict['h'], sheriff_dict['e'], sheriff_dict['r'], sheriff_dict['i'],
               int(sheriff_dict['f'] / 2))


print(sheriff())