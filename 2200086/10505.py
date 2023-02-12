# 소득 불균형

T = int(input())
for i in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    average = sum(a) / N
    cnt = 0
    for j in a:
        if j <= average:
            cnt += 1
    print(f'#{i} {cnt}')