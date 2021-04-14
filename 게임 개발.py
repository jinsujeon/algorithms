import random
N , M = map(int,input().split())
start_point_0,start_point_1 , direction = list(map(int,input().split()))

def make_1row():
    zero_counts = random.randint(0,M)
    one_counts = M - zero_counts
    my_list = [0]*zero_counts + [1]*one_counts
    random.shuffle(my_list)
    return my_list
maps = []
for _ in range(N):
    inf_list = make_1row()
    maps.append(inf_list)

print(maps)
print(maps[start_point_0][start_point_1])
counts = 1

if direction == 0: #북쪽이면
    if maps[start_point_0-1][start_point_1 ] == 0:      # 땅이면
        start_point_0 -=1
        counts +=1
    elif maps[start_point_0-1][start_point_1 ] == 1:      # 바다면
        direction +=3

elif direction == 1: #동쪽이면
    if maps[start_point_0][start_point_1 +1] == 0:      # 땅이면
        start_point_1 +=1
        counts +=1
    elif maps[start_point_0][start_point_1 +1] == 1:  #바다면
        direction -= 1
elif direction == 2: #남쪽이면
    if maps[start_point_0 +1][start_point_1 ] == 0:  # 땅이면
        start_point_0 += 1
        counts += 1
    elif maps[start_point_0][start_point_1 - 1] == 1:  # 바다면
        direction -= 1

elif direction == 3: #서쪽이면
    if maps[start_point_0][start_point_1 - 1] == 0:  # 땅이면
        start_point_1 += 1
        counts += 1
    elif maps[start_point_0][start_point_1 - 1] == 1:  # 바다면
        direction -= 3

print(start_point_0,start_point_1,direction)