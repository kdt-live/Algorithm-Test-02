T = int(input())
cnt = 0
cnt1 = 0
for t in range(T):
    num = list(map(int,input().split()))
    for n in num:
        cnt1 += 1
        if cnt1%2 == 1 :
            cnt += n*2
        elif cnt1%2 == 0 :
            cnt += n
    if cnt%10 != 0 :
        b = 10 - (cnt%10)
    elif cnt%10 == 0:
        b = 0
    print(f'#{t+1} {b}')
         
        

