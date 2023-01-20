# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    n = int(input())
    income = list(map(int, input().split()))
    average = sum(income)/n
    cnt = 0
    for i in income:
        if i <= average:
            cnt += 1
    print(f'#{t} {cnt}')
