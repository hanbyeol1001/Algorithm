# 첫 번째 시도

# N = int(input())
# num_list = []
# for _ in range(N):
#     n = int(input())
#     num_list.append(n)
#     num_list.sort()

# for i in num_list:
#     print(i)

# 제출했더니 메모리 초과 발생


########################################################
# 두 번째 시도
# 리스트 내 각 원소의 갯수를 세어 출력하는 방법으로 재시도

# N = int(input())
# cnt = [0 for _ in range(max(num_list)+1)]  # 0~최댓값
# for i in num_list:
#     cnt[i] += 1
# for num in range(len(cnt)):
#     for _ in range(cnt[num]):
#         print(num, end='\n')

# 메모리 초과 발생

########################################################
# 세 번째 시도
# append하지 말고 처음부터 입력으로 들어올 수 있는 가능한
# 큰 수를 기준으로 cnt리스트를 미리 만들어놓는 걸로 재시도

N = int(input())
cnt = [0] * (10000+1)
for _ in range(N):
    num = int(input())
    cnt[num] += 1

for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    for _ in range(cnt[i]):
        print(i)
