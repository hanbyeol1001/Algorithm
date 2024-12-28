N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
t = 0
for i in size:
    if i%T == 0:
        t += i//T
        continue
    t += i//T + 1
print(t)
print(N//P, N%P)