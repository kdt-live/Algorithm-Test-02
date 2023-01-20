T = int(input())
for i in range(1, T + 1):
    N = int(input())
    a = list(map(int,input().split()))
    b = sum(a)/N
    for number in a:
        if number <= b:    
            number = []
            print(f'#{i} {len(number)}')