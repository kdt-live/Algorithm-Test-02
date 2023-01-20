e = int(input())

for i in range(1,e+1):
    d=0
    a,b,c = map(int,input().split())

    if a == b:
        d+=c
    elif a == c:
        d+=b
    elif b == c:
        d+=a

    print(f'#{i} {d}')

