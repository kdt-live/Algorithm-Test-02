a = int(input())

for i in range(1,a+1):
    c=0
    d=1
    b = list(map(int,input().split()))
    for j in b:
        if d%2==1:
            c+=j*2
            d+=1
        else:
            c+=j
            d+=1

    q = 10-(c%10)
    if q == 10:
        print(f'#{i} 0')
    else:
        print(f'#{i} {q}')

 