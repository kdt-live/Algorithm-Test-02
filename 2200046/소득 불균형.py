t = int(input())

for i in range(t):
    n = int(input())
    income = list(map(int, input().split()))
    avg = sum(income) / n
    cnt = 0

    for num in income:
        if num <= avg:
            cnt += 1

    print(f'#{i + 1} {cnt}')