import sys

n = int(sys.stdin.readline().strip())

members = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append([int(age), name])

members.sort(key=lambda x: x[0])

for m in members:
    print(m[0], m[1])