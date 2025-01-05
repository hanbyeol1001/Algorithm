from statistics import mean, median, multimode

n = int(input())
value = []
for i in range(n) :
    k = int(input())
    value.append(k)
value.sort()

# 산술평균
print(round(mean(value)))

#  중앙값
print(median(value))

# 최빈값
mode = multimode(value)
if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])

# 범위
print(value[-1]-value[0])