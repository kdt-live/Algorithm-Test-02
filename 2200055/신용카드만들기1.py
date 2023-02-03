T=int(input())
for i in range (1,T+1):
    x=list(map(int,input().split()))
    sum=0
    for j in range (len(x)):
        if j%2==0:
           sum+=x[j]*2
        else:
            sum+=x[j]
    if sum%10==0:
        print(f'#{i} 0')
    else:
        ans=10-(sum%10)
        print(f'#{i} {ans}')            