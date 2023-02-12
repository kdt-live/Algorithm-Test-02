# 직사각형 길이 찾기

T = int(input())
for i in range(1, T+1):
    a, b, c = list(map(int, input().split()))
    s = {a, b ,c}
    d = a + b + c
    if a == b == c:
        print(f'#{i} {a}')
    else:
        print(f'#{i} {(sum(s)*2)-(d)}')