# 3456번 - 직사각형 길이 찾기
T = int(input())

for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    d = 0
    if a == b:
        d = c
    else:
        if b == c:
            d = a
        else:
            d = b
            
    print(f'#{tc} {d}')