T = int(input())
for _ in range(T):
    R, P = input().split()
    R = int(R)
    output = ''
    for p in P:
        output += R*p
    print(output)