# 소득 불균형

T= int(input())
for t in range(1,T+1):
    p = int(input())
    money = list(map(int,input().split()))
    
    avg = sum(money) // p
    count = 0

    for i in money:
        if i <= avg:
            count +=1

    print(f'#{t} {count}')

