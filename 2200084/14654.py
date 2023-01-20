T = int(input())
first = ['3', '4', '5', '6', '9']
for i in range(1, T+1):
    card_num = input()
    cnt = 0
    if card_num[0] in first:
        for j in card_num:
            if j != '-':
                cnt += 1
    if cnt == 16:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
        