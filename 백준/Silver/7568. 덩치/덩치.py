import sys

n = int(input())

# info: 몸무게와 키 리스트를 담은 리스트
info = [[], []]
for _ in range(n):
    kg, cm = map(int, sys.stdin.readline().split())
    info[0].append(kg)
    info[1].append(cm)

rank_list = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i==j:
            pass
        elif info[0][j] > info[0][i] \
            and info[1][j] > info[1][i]:
            cnt += 1
    rank_list.append(cnt)

for rank in rank_list:
    print(rank, end=' ')