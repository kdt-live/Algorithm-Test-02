T = int(input())

for t in range (T):
    square = list(map(int, input().split()))

    for sqr in square:
        if (square.count(sqr) % 2 == 1):
            length = sqr
    
    print(f'#{t+1} {length}')