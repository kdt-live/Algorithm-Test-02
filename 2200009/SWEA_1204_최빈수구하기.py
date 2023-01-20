i_t = int(input())
for i_1 in range(i_t):
    i_t_c = int(input())
    lst_score = list(map(int, input().split()))
    dict_score = {}
    for i_2 in lst_score:
        dict_score[i_2] = dict_score.get(i_2, 0) + 1
    lst_maxkey = [key_1 for key_1, value_1 in dict_score.items() if value_1 == max(dict_score.values())]
    print(f'#{i_t_c} {max(lst_maxkey)}')