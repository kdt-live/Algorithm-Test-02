# 소득 불균형
T = int(input())

for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    for n in num:
        if n <= sum(num) // N:
            cnt += 1
    print(f'#{t} {cnt}')