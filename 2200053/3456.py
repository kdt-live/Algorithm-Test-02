# 직사각형 길이 찾기
T = int(input())

for t in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print(f'#{t} {c}')
    elif a == b == c:
        print(f'#{t} {a}')
    elif a == c and a != b:
        print(f'#{t} {b}')
    elif b == c and a != b:
        print(f'#{t} {a}')