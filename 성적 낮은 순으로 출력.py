n = int(input())

inf_dict = {}
for i in range(n):
    ele = input().split(' ')
    inf_dict[ele[0]] = ele[1]

inf_dict = dict(sorted(inf_dict.items(),key = lambda x : x[1]))

for i in inf_dict.keys():
    print(i , end= ' ')