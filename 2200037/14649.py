#신용카드 만들기 1
T = int(input())
for i in range(1,T+1):
    num = list(map(int,input().split()))
    sum1, sum2 = 0,0
    for j in range(0,len(num)):
        if j % 2 == 0:
            sum1 += (num[j]*2)
        elif j % 2 == 1:
            sum2 += num[j]
    n = sum1 + sum2
    
    for j in range(10):
        if (n+j)%10 == 0:
            test = j
    print(f'#{i} {test}')