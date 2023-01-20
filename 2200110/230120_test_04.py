T = int(input())
for t in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    cnt = 0

    for i in income:
        if i <= sum(income)/N:
            cnt += 1
    print(f'#{t} {cnt}')
