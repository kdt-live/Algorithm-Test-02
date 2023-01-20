t = int(input())

for i in range(1, t+1):
    nums = list(map(int,input().split()))
    answer = min(nums, key=nums.count)
    print(f'#{i} {answer}')