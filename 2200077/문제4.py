# 불균등 소득

T = int(input())

for t in range(T):
    test_case = int(input())
    income = list(map(int, input().split()))
    average = sum(income) // test_case
    cnt = 0

    for i in income:
        if i <= average:
            cnt += 1
    print(f'#{t+1} {cnt}')