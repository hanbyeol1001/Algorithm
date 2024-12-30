n = int(input())
target, stack = [], [1]
push_pop = ['+']
result = []
push_num = 2
for _ in range(n):
    num = int(input())
    target.append(num)
    if len(stack) < 1:
        stack.append(push_num)
        push_num += 1
        push_pop.append('+')
    while stack[-1] < num:
        stack.append(push_num)
        push_num += 1
        push_pop.append('+')
    if stack[-1] == num:
        p = stack.pop(-1)
        result.append(p)
        push_pop.append('-')

if result == target:
    for i in push_pop:
        print(i, end='\n')
else:
    print('NO')