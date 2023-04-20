T = int(input())
cnt = 0
for t in range(T):
    N = int(input())
    num = list(map(int,input().split()))
    num_everage = (sum(num)/N)
    for i in num :
        if i <= num_everage:
            cnt += 1
    print(f'{t+1} {cnt}')
    cnt = 0