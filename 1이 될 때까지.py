'''어떠한 수 N이 1이 될 때 까지  반복한다. 두번째 연산은 N이 K로 나눠 떨어질 떄만 가능
1. N에서 1을 뺌
2. N을 K로 나눔
'''
N, K = map(int,input().split())
print('N is' , N , 'K is' , K)
results = 0
while True:
    if N % K == 0:
        N = N // K
        results += 1
    elif N % K != 0:
        N = N -1
        results += 1

    if N ==1:
        break
print(results)