n = int(input())
answer = 0
while n > 0:
    if n % 5 == 0:
        answer += n // 5
        n -= n
        break
    elif n % 3 == 0:
        if n//3 > 5:
            answer += 3
            n -= 3*5
            continue
        answer += n // 3
        n -= n
        break
    else:
        if n > 5:
            answer += 1
            n -= 5
        else:
            answer += 1
            n -= 3
if n == 0:
    print(answer)
else:
    print(-1)