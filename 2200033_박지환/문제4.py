# 소득 불균형

T = int(input())

for i in range(T):
    test_case = int(input())
    earning_list = list(map(int, input().split()))

    cnt = 0
    for j in range(test_case):
        if earning_list[j] <= sum(earning_list)/test_case: # 소득이 소득평균 이하일 때
            cnt += 1
    
    print(f'#{i+1} {cnt}')