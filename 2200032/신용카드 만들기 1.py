T = int(input())
for test_case in range(1, T+1):
    lst = [0] + [int(x) for x in input().split()]
    odd = even = N = sum = 0
    for i in range(len(lst)):
        if i & 1:
            odd += lst[i] * 2
        else:
            even += lst[i]
    if (even+odd) % 10:
        N = 10 - ((odd + even) % 10)
    else:
        N = 0    
    print(f'#{test_case} {N}')