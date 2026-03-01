def solution(progresses, speeds):
    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        if (100-p) % s == 0:
            day = (100-p)//s
        else:
            day = (100-p)//s + 1
        days.append(day)
    
    index = 0
    print(f"days: {days}")
    
    while index < len(days):
        criteria = days[index]
        count = 0
        while index < len(days) and days[index] <= criteria:
            count += 1
            index += 1
        answer.append(count)
        
    
    return answer