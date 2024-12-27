nums = list(map(int, input().split()))
sum = 0
for n in nums:
    sum += int(n)**2
print(sum%10)