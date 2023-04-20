i_t = int(input())
for i_1 in range(i_t):
    lst_edge = list(map(int, input().split()))
    dict_edge = {}
    for i_2 in lst_edge:
        dict_edge[i_2] = dict_edge.get(i_2, 0) + 1
    i_result = [key_1 for key_1, value_1 in dict_edge.items() if value_1 == min(dict_edge.values())].pop()
    print(f'#{i_1 + 1} {i_result}')