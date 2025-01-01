N = int(input())
cnt = [0] * (10000+1)
for _ in range(N):
    num = int(input())
    cnt[num] += 1

for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    for _ in range(cnt[i]):
        print(i)