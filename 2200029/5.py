import sys
sys.stdin = open("예제입력.txt", "r")

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    i = 0
    num_sum = 0
    while i < 7:
        num_sum += (nums[2 * i] * 2) + nums[2 * i + 1]
        i += 1
    num_sum += nums[14] * 2

    N = 10 - (num_sum % 10)
    if N == 10:
        N = 0
    print(f'#{t} {N}')


