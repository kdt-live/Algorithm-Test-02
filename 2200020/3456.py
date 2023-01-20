T = int(input())
for test_case in range(1, T + 1):
    xy_list = []
    for l in list(map(int, input().split())):
        if l not in xy_list:
            xy_list.append(l)
        else:
            xy_list.remove(l)
    print(f'#{test_case} {xy_list[0]}')