t = int(input())

for i in range(1, t+1):
    num = int(input())
    income = list(map(int, input().split()))
    average = sum(income) / len(income)
    answer = 0
    for v in income:
        if v <= average:
            answer += 1
    print(f'#{i} {answer}')