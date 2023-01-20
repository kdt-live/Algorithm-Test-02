#소득 불균형
T = int(input())
for i in range(1,T+1):
    n = int(input())
    cnt = 0
    n_list = list(map(int,input().split()))
    avg = sum(n_list) / n
    for j in n_list:
        if j <= avg:
            cnt+=1
    print(f'#{i} {cnt}')