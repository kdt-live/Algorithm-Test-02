# 직사각형 길이

T = int(input())

for t in range(T):
    a, b, c = map(int, input().split())

    if a == b == c:
        print(f'#{t+1} {a}')
    elif a == b and a != c:
        print(f'#{t+1} {c}')
    elif a != b and a == c:
        print(f'#{t+1} {b}')
    else:
        print(f'#{t+1} {a}')