N = int(input())

# 문제에 단순히 접근: 생성자를 찾자
exist = 0
for i in range(1, N):
    sum_num = sum([int(x) for x in str(i)])
    if N-sum_num == i:
        exist = i
        break
print(exist)