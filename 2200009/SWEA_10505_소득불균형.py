i_t = int(input())
for i_1 in range(i_t):
    i_n = int(input())
    lst_nums = list(map(int, input().split()))
    i_count = 0 
    for i_2 in lst_nums:
        if i_2 <= sum(lst_nums) / len(lst_nums):
            i_count += 1
    print(f'#{i_1 + 1} {i_count}')