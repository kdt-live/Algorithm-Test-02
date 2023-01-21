import sys
sys.stdin = open('input_10505.txt', 'r')

# 제출한 답
T = int(input())

for t in range(1, T+1):
    p = int(input())
    a = list(map(int, input().split()))
    avg = sum(a)/p
    result = 0
    for i in a:
        if i <= avg:
            result +=1
    print(f'#{t} {result}')