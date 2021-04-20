from random import random

N, M = map(int, input().split(' '))
print('N', N)
print('M', M)

path_matrix = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]

def bfs(x,y):
    queue = deque()
    