#10505 소득 불균형

T = int(input())
for i in range(1, T + 1):
    x = int(input())
    income = list(map(int, input().split()))
    avr = sum(income) / x
    cnt = 0
    for j in income:
        if j <= avr:
            cnt += 1
    print(f"#{i} {cnt}")