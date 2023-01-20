i_t = int(input())
lst_start = ['3', '4', '5', '6', '9']
for i_1 in range(i_t):
    s_card = input()
    s_newcard = ''
    for s_1 in s_card:
        if s_1 != '-':
            s_newcard += s_1
    if (s_newcard[0] in lst_start) * (len(s_newcard) == 16): 
        print(f'#{i_1 + 1} 1')
    else:
        print(f'#{i_1 + 1} 0')