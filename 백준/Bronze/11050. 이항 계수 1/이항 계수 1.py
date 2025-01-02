n, k = map(int, input().split())
answer = 1
for i in range(n, n-k, -1):
    answer *= i
div = 1
for i in range(k, 0, -1):
    div *= i
print(answer//div)