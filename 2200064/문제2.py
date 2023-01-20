# 직사각형 길이찾기

T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    d = 0
    if a == b == c:
        d = a
    elif a == b:
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a
    print(f'#{i}', d)