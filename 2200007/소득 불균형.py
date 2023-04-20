T = int(input())
avg = 0
cnt = 0

for t in range (1, T+1) :
    N = int(input())
    n = list(map(int,input().split()))
    avg = sum(n)/N
    for i in range(N) :
        if n[i] <= avg :
            cnt += 1
    print(f"#{t} {cnt}")
    cnt = 0