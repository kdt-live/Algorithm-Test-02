T = int(input()) 

for t in range(1, T+1) :
    n = int(input()) 
    li = list(map(int, input().split()))

    avg = sum(li) / n
    cnt = 0

    for i in li :
        if avg >= i :
            cnt += 1
    print(f'#{t} {cnt}')        