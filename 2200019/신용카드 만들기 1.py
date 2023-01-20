T = int(input())

for i in range(1,T+1):
    n = list(map(int,input().split()))
    cnt = 0
    for j in range(15):
        if (j+1)%2 == 1:
            cnt += n[j]*2
        else:
            cnt += n[j]
    
    if cnt % 10 == 0 :
        print(f'#{i} 0')
    else:
        print(f'#{i} {10-(cnt%10)}')