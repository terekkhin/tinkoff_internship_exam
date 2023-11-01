# task_4

# На Диком западе ходят купюры номиналами a1, a2, ..., am долларов. Однажды ковбой Джо решил ограбить банк.
# Он выбрал очень неудачный момент для ограбления, ведь сейчас в банке находятся ровно
# по две купюры каждого существующего номинала.
# Ковбой Джо хочет украсть ровно n долларов, ни долларом больше, ни долларом меньше.
# Помогите ему или сообщите, что его план неосуществим.

def generate_combinations(arr, target_sum, curr_sum, path, result):
    if curr_sum > target_sum:
        return

    if curr_sum == target_sum:
        result.append(path.copy())
        return

    for i in range(len(arr)):
        curr_num = arr[i]
        curr_sum += curr_num
        path.append(curr_num)
        generate_combinations(arr[i + 1:], target_sum, curr_sum, path, result)
        curr_sum -= curr_num
        path.pop()

def find_combinations():
    target_sum, n = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    arr += arr
    generate_combinations(arr, target_sum, 0, [], result)
    return result

ans = find_combinations()
if ans:
    print(len(ans[0]))
    print(*ans[0])
else:
    print(-1)