T = int(input())

for t in range (T):
    N = int(input())
    incomes = list(map(int, input().split()))
    count = 0

    avg_income = sum(incomes) / N

    for income in incomes:
        if (income <= avg_income):
            count += 1

    print(f'#{t+1} {count}')