n = int(input())
s = input()
H = 0
r, M = 31, 1234567891
for i in range(n):
    a = ord(s[i]) - ord('a') + 1
    H += (a*r**i) % M
print(H)