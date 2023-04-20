T = int(input())

for t in range(1, T+1):
    N = int(input())
    amounts = list(map(int, input().split()))

    avg = sum(amounts) / N
    lower_income = []
    for income in amounts:
        if income <= avg:
            lower_income.append(income)
    
    print(f'#{t} {len(lower_income)}')