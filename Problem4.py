t = int(input())
for i in range(1, t+1) :
    a= list(map(int, input().split()))
    cnt = 0
    n =0
    for j in range(0, len(a)) :
        if j % 2 == 1 :
            cnt += a[j]
        else :
            cnt += (a[j]*2)
    if cnt % 10 == 0 :
        print(f"#{i} {0}")
    else :
        n = cnt % 10
        print(f"#{i} {10-n}")