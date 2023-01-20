T = int(input())
for t in range(1, T+1):
    Number = list(map(int, input().split()))
    tmp_ = []
    result = 0
    x = 0
    for n in range(1, 16):
        if n%2 == 1:
            result += 2*Number[n-1]
        else:
            tmp_.append(Number[n-1])
    tmp = result + sum(tmp_)
    while True:
        if tmp%10 == 0:
            print(f'#{t} {x}')
            break
        else:
            tmp += 1
            x += 1
            