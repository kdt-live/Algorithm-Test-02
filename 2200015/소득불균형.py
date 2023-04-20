a = int(input())

for i in range(1,a+1):
    q=0
    w= 0
    b= int(input())
    c = list(map(int,input().split()))
    q = sum(c)//b
    for j in c:
        if j <= q:
            w+=1
    print(f'#{i} {w}')


    
