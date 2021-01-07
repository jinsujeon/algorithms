N =int(input())
plans = list(map(str,input().split()))
print(N)
print(plans)

start_point =[1,1]
print('start point is ', start_point)

for i in plans:
    if i == 'U':
        if start_point[0] != 1:
            start_point[0] -= 1
        else:
            continue
    elif i == 'D' :
        if start_point[0] != N:
            start_point[0] += 1
        else:
            continue
    elif i == 'R':
        if start_point[1] != N:
            start_point[1] += 1
        else:
            continue
    elif i == 'L':
        if start_point[1] != 1:
            start_point[1] -= 1
        else:
            continue


print(" ".join(map(str,start_point)))