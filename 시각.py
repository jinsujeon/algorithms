from datetime import datetime

H = int(input())

count = 0
for h in range(H+1):
    for m in range(60):
        for s in range(60):
            total_time = '{}:{}:{}'.format(h,m,s)
            if '3' in total_time:
                count +=1
print(count)