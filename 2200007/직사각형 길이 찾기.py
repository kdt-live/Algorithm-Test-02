T = int(input())
d = 0

for t in range (1, T+1) :
    a, b, c = list(map(int,input().split()))
    if a == b :
        d = c
        print(f"#{t} {d}")
    elif a == c :
        d = b
        print(f"#{t} {d}")
    elif b == c :
        d = a
        print(f"#{t} {d}")
