def fact_str(num):
    result = 1
    for i in range(num, 1, -1):
        result *= i
    return str(result)
n = int(input())
fact = fact_str(n)
cnt = 0
for f in fact[::-1]:
    if f != '0':
        break
    cnt += 1
print(cnt)