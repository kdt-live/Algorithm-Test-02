import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums_average = sum(nums) / len(nums)
    cnt = 0
    for num in nums:
        if num <= nums_average:
            cnt += 1
    print(f'#{t} {cnt}')