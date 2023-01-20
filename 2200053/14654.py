# 신용카드 만들기 2

T = int(input())

for  t in range(1, T+1):
    card_num = input()
    #print(card_num[0])
    if card_num[0] in '3, 4, 5, 6, 9' and len(card_num.replace('-', '')) == 16:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')


# n = '7840-2471-3391-9776'
# print(len(n.replace('-', '')))