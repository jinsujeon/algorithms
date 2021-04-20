array=  [7,5,9,0,3,1,6,2,4,8]

for idx in range(len(array)):
    min_idx = idx
    print('idx',idx)
    for j in range(idx+1 , len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
            print('m_idx',min_idx)

    array[idx] , array[min_idx] = array[min_idx] , array[idx]

print(array)
