n = int(input())
n_str = str(n-1)
limit = int(n_str+'666')
cnt = 0
for i in range(666, limit+1):
    if '666' in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break