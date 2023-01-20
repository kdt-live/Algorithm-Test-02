T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))

    operation_1 = sum(nums[::2]) * 2
    operation_2 = sum(nums[1::2])
    N = 10 - ((operation_1 + operation_2) % 10)
    N %= 10

    print(f'#{t} {N}')