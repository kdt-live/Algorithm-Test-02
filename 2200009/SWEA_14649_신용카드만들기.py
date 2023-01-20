i_t = int(input())
for i_1 in range(i_t):
    lst_nums = list(map(int, input().split()))
    sum = 0
    for i_2 in lst_nums[::2]:
        sum += i_2  * 2
    for i_3 in lst_nums[1::2]:
        sum += i_3
    i_luhn = (10 - sum%10)%10
    print(f'#{i_1 + 1} {i_luhn}')
