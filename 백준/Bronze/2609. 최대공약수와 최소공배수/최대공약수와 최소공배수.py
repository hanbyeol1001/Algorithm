a, b = map(int, input().split())

# 최대공약수: the greatest commom facter
gcf = 0
m = min(a, b)
for i in range(m, 0, -1):
    if a%i == 0 and b%i == 0:
        gcf = i
        break

# 최소공배수: the least common multiple
lcm = 0
# "두 수의 곱 = 최대공약수 * 최소공배수"임을 이용
lcm = a * b // gcf  # 무조건 나누어떨어지므로 몫을 반환.(int)

print(gcf, lcm, sep='\n')