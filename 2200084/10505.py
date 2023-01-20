T = int(input())
for x in range(1, T+1):
    N = int(input())
    money = list(map(int, input().split()))
    money_avr = sum(money) / N
    cnt = 0
    for i in money:
        if i <= money_avr:
            cnt += 1
    print(f'#{x} {cnt}')