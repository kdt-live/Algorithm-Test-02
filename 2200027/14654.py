t = int(input())

for i in range(1, t+1):
    nums = input()
    nums = nums.replace("-", "")
    if len(nums) != 16:
        print(f'#{i} 0')
    elif nums[0] not in "34569":
        print(f'#{i} 0')
    else:
        print(f'#{i} 1')