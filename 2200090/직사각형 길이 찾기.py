for t in range(1, int(input())+1):
    a, b, c = map(int, input().split())
    d = 0
    if a == b:
        d += c
    elif a == c:
        d += b
    else:
        d = a
    print(f'#{t} {d}')