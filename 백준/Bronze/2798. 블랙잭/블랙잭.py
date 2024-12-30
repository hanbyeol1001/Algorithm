from itertools import combinations
# 순열, 조합 라이브러리 itertools
## combinations 함수: 조합
## permutations 함수: 순열

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

# 가능한 카드의 조합을 모두 순회
for i in combinations(cards, 3):
    if sum(i) <= M:
        if answer < sum(i):
            answer = sum(i)
print(answer)