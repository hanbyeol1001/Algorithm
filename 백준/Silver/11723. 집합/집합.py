import sys

m = int(input())
S = set()
for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        x = command[1]
        S.add(x)
    elif command[0] == 'remove':
        x = command[1]
        if x in S:
            S.remove(x)
    elif command[0] == 'check':
        x = command[1]
        if x in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        x = command[1]
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif command[0] == 'all':
        S = set([str(i) for i in range(1, 21)])
    elif command[0] == 'empty':
        S = set()