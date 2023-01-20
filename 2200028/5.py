T = int(input())
for t in range(1, T+1):

    a, b, c = map(int,input().split())
    d = 0

    if a == b:
        d = c
    elif b == c:
        d = a
    elif a == c:
        d = b
    print(f'#{t} {d}')