n, m = map(int, (input().split()))
dont_hear, dont_see = set(), set()
for _ in range(n):
    name = input()
    dont_hear.add(name)
for _ in range(m):
    name = input()
    dont_see.add(name)

dont_hear_see = list(dont_hear & dont_see)
dont_hear_see.sort()

print(len(dont_hear_see))
for i in dont_hear_see:
    print(i)