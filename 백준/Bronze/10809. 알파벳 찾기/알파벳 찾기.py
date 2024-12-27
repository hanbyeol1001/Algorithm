S = input()
n = ord('z')-ord('a') + 1

answer = [-1 for _ in range(n)]

for i, s in enumerate(S):
    idx = ord(s)-ord('a')
    if answer[idx] >= 0:
        continue
    answer[idx] = i

for num in answer:
    print(num, end=' ')