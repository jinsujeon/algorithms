import numpy as np
N , M = map(int,input().split())

values= 0
for _ in range(N) :
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(values,min_value)

print(result)