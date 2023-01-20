T=int(input())

for s in range(T):
    n= int(input())
    lst=list(map(str,input().split()))
    d={}
    for j in lst:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    d_arr=dict(sorted(d.items(), key=lambda x:x[1], reverse=True)) 
    print(f'#{s+1} {list(d_arr)[0]}')