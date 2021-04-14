from random import random

N,M = map(int,input().split(' '))

ice_matrix = []

for _ in range(N):
    ice_matrix.append([0 if random() <=0.5 else 1 for _ in range(M)])

print(ice_matrix)
def dfs(x,y):
    if x<=-1 or x >=N or y <=-1 or y >=M :
        return False
    if ice_matrix[x][y] == 0:
        ice_matrix[x][y] =1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result +=1

print(result)