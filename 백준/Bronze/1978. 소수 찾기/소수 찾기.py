N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for n in nums:
    if n == 1:
        continue
    temp = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            temp += 1
    if temp == 0:
        cnt += 1
print(cnt)