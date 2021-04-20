n = int(input())

array = []
for i in range(n):
    ele = int(input())
    array.append(ele)

array.sort()
array = array[::-1]
print(array)