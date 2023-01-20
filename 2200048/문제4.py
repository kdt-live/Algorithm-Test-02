T = int(input())
for i in range(1,T + 1):
    n_avg = 0
    n = int(input())
    inc = list(map(int,input().split()))
    avg_n = int(sum(inc) / n)
    for s in inc:
        if s <= avg_n:
            n_avg += 1
    print(f'#{i} {n_avg}')
