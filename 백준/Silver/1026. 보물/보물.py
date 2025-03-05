def func(N, A, B):
    '''
    S의 최솟값만 출력하면 되므로, 정렬할 필요는 없다.
    A와 B를 각각 내림차순, 오름차순 한 뒤 S를 구하면 된다.
    '''
    A.sort()
    B.sort(reverse=True)
    S = 0
    for i in range(N):
        S += A[i]*B[i]
    return S

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = func(n, a, b)
print(s)