# 직사각형 길이 찾기
T = int(input())
for i in range(1, T + 1):
    a, b, c = list(map(int,input().split()))
    d = c or b or a
    if a == b:
        c == d
        print(f'#{i} {d}')
    elif a == c:
        b == d
        print(f'#{i} {d}')
    elif a == d:
        b == c
        print(f'#{i} {d}')