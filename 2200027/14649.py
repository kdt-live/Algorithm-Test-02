t = int(input())

for i in range(1, t+1):
    nums = list(map(int, input().split()))
    num_sum = 0
    answer = 0
    for j in range(len(nums)):
        if j % 2 == 0: #홀수
            num_sum += nums[j] * 2
        else:
            num_sum += nums[j]
    if num_sum % 10 == 0:
        answer = 0
    else:
        answer = 10 - (num_sum % 10)
    print(f'#{i} {answer}')