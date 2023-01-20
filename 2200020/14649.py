T = int(input())
for test_case in range(1, T + 1):
    odd, even, n = 0, 0, 0
    for index, num in enumerate(list(map(int, input().split())), start=1):
        if index % 2 == 1:
            odd += num*2
        else:
            even += num
    if (odd+even)%10 != 0:
        n = 10-(odd+even)%10
    print(f'#{test_case} {n}')