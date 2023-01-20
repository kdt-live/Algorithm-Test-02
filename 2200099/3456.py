T = int(input())
for t in range(1, T+1):
    a,b,c = list(map(int, input().split()))
    if a == b:
        print(f'#{t} {c}')
    elif b == c:
        print(f'#{t} {a}')
    else:
        print(f'#{t} {b}')
    