t = int(input())

for i in range(1, t+1):
    nums = list(map(int, input().split()))
    num_sum = 0 #숫자합
    N = 0
    for j in range(len(nums)):
        if j % 2 == 0: #홀수
            num_sum += nums[j] * 2
        else:
            num_sum += nums[j]
    if num_sum % 10 == 0: #숫자합이 10으로 나누어 떨어지면
        N = 0
    else:
        N = 10 - (num_sum % 10)
    print(f'#{i} {N}')