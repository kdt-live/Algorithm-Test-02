# 소득 불균형

T = int(input())

for i in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    income_avg = sum(income)/N
    count = 0
    for j in income:
        if j <= income_avg:
            count += 1
    print(f'#{i} {count}')