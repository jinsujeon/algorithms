n = int(input())
A = input().split()
M = int(input())
a = input().split()


print('A' ,A)
print('a', a)


############################풀이 1#######################
for ele in a:
    if ele in A :
        print('yes')
    else :
        print('no')


############################풀이 2#######################
def binarysearch(array,target,start,end):
    if start > end :
        return None
    mid = (start + end) //2

    if array[mid] == target :
        return mid

    elif array[mid] < target :
        return binarysearch(array,target,mid+1,end)

    elif array[mid] > target:
        return binarysearch(array,target,start,mid-1)

for ele in a:
    result = binarysearch(A,ele,0,n-1)
    if result == None:
        print('no')
    else :
        print('yes')

############################풀이 3#######################
array = [0] * 1000001
for ele in A:
    array[int(ele)] = 1

for ele in a:
    if array[int(ele)] == 1:
        print('yes')
    else:
        print('no')