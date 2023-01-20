T = int(input())
for test_case in range(1, T + 1):
    test_case_num = int(input())
    test_case_dict = {}
    for num in input().split():
        if num not in test_case_dict:
            test_case_dict[num] = 1
        else:
            test_case_dict[num] += 1
    print(f'#{test_case_num} {sorted(test_case_dict.items(), key = lambda x: (x[1], x[0]), reverse = True)[0][0]}')