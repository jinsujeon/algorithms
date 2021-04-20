array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

new_array = [0] * (max(array) + 1)

print(new_array)

for i in array:
    new_array[i] += 1


inf_list = []
for num, i in enumerate(new_array):
    ele = [num] * i
    inf_list.extend(ele)

print(inf_list)