import numpy as np
N = input()
start_point = (N[0],int(N[1]))
alphabet = ['a','b','c','d','e','f','g','h']
nums = range(1,9)
inf_dict = {}
for num,a in enumerate(alphabet):
    inf_dict[a] = num+1
change_point = [int(inf_dict[N[0]]),int(N[1])]

actions = ['UUL','UUR','LLU','LLD','DDL','DDR','RRU','RRD']


def check_action(point):
    if (0 < point[0]) & (point[0] <= 8) & (0 < point[1]) & (point[1] <= 8):
        return 1
    else:
        return 0

count = 0
for action in actions:
    if action == 'UUL':
        change_point[1] -=2
        change_point[0] -=1
        result = check_action(change_point)
        change_point =  [int(inf_dict[N[0]]),int(N[1])]
        print(result)
        count += result

    elif action =='UUR':
        change_point[1] -= 2
        change_point[0] += 1
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result
    elif action =='LLU':
        change_point[1] -= 1
        change_point[0] -= 2
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result
    elif action == 'LLD':
        change_point[1] += 1
        change_point[0] -= 2
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result
    elif action == 'DDL':
        change_point[1] += 2
        change_point[0] -= 1
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result
    elif action == 'DDR':
        change_point[1] += 2
        change_point[0] += 1
        print(change_point)
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result
    elif action == 'RRU':
        change_point[1] -= 1
        change_point[0] += 2
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result
    elif action == 'RRD':
        change_point[1] += 1
        change_point[0] += 2
        result = check_action(change_point)
        change_point = [int(inf_dict[N[0]]), int(N[1])]
        print(result)
        count += result

print(count)