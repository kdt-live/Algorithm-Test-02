t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    mean = sum(nums) / n
    cnt = 0
    
    for num in nums:
        if num <= mean:
            cnt += 1
    
    print(f'#{i+1} {cnt}')