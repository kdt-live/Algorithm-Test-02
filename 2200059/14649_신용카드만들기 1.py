# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in nums[0:15:2]:
        odd += i
    for i in nums[1:15:2]:
        even += i
    N = (10 - ((odd*2+even) % 10)) % 10
    print(f'#{t} {N}')
