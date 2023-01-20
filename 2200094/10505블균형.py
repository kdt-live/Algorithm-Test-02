T = int(input())


for t in range(1, T+1):
    cnt = int(input())
    money = list(map(int, input().split()))
    avg = int(sum(money)/len(money))
    result = 0
    for i in money:
        if i <= avg:
            result += 1
    print(f'#{t} {result}')
        