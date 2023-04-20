T=int(input())
for i in range (1,T+1):
    x=list(map(int,input().split()))
    if len(set(x))==1:
        print(f'#{i} {x[0]}')
    else:
        ans=2*sum(set(x))-sum(x)
        print(f'#{i} {ans}')