T = int(input())
for t in range(1, T + 1):
    nums = list(input().split())
    for num in nums:
        if nums.count(str(num)) % 2 == 1:
            print(f'#{t} {num}')
            break
        

