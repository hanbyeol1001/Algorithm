nodes = list(map(str, input().split()))
ascend = [str(i) for i in range(1, 9)]
descend = [str(i) for i in range(8, 0, -1)]

if nodes==ascend:
    print('ascending')
elif nodes==descend:
    print('descending')
else:
    print('mixed')