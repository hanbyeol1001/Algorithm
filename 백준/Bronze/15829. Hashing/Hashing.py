n = int(input())
s = input()
H = 0
r = 31
for i in range(n):
    a = ord(s[i]) - ord('a') + 1
    H += a * r ** i
print(H%1234567891)