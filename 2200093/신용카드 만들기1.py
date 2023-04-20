T = int(input())

for i in range(T):
    num = list(map(int, input().split()))
    sum = 0

    for j in range(0, 15):
        if j % 2 == 0:
            sum += num[j]*2
        else:
            sum += num[j]

    N = 10 - (sum % 10)
    if N == 10:
        print(f'#{i+1} 0')
        sum = 0
    else:
        print(f'#{i+1} {N}')
        sum = 0