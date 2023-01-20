import sys
sys.stdin = open('input_14649.txt', 'r')

# 제출한 답
T = int(input())

for t in range(1, T+1):
    a = list(map(int, input().split()))
    sum_ = sum(a[::2])*2 + sum(a[1::2])
    result = (10-sum_%10)%10
    print(f'#{t} {result}')