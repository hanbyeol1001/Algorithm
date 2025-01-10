N, M = map(int, input().split())
dogam = dict()
poketmons = list()
for i in range(1, N+1):
    poketmon = input()
    dogam[poketmon] = i
    poketmons.append(poketmon)
for _ in range(M):
    problem = input()
    if problem.isalpha():
        print(dogam.get(problem))
    else:
        print(poketmons[int(problem)-1])