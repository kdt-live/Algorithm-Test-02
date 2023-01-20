a= int(input())
for i in range(a):
    num = int(input())
    cnt = 0
    l = list(map(int,input().split()))
    for j in l:
        if j<=sum(l)/num:
            cnt+=1
    print(f'#{i+1} {cnt}')