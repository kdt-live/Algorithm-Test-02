for t in range(1, int(input())+1):
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = list(map(int, input().split()))
    odd = (a*2) + (c*2) + (e*2) + (g*2) + (i*2) + (k*2) + (m*2) + (o*2)
    even = b + d + f + h + j + l + n
    result = odd + even
    if result%10 == 0:
        n = 0
    elif result%10 != 0:
        n = 10 - (result%10)%10
    else:
        n = 0
        
    print(f'#{t} {n}')