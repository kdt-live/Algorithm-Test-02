# 대칭만들기
# 나머지 변의 길이 출력

T = int(input())

for t in range(1, T+1):
    a, b, c = list(map(int, input().split()))
    d = 0
    if a==b:
        d = c
        print(f'#{t} {d}')
    elif b==c:
        d = a
        print(f'#{t} {d}')
    elif a==c:
        d = b
        print(f'#{t} {d}')
    elif a==b==c:
        b = a
        print(f'#{t} {d}')