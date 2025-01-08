n, k = map(int, input().split())
coins = []
for _ in range(n):
    won = int(input())
    coins.append(won)

cnt = 0
for i in coins[::-1]:
    while k >= i:
        k -= i
        cnt += 1
    if k == 0:
        break
print(cnt)