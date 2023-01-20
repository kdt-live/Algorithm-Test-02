# 신용카드 만들기 2
T = int(input())

for t in range(1, T+1):
    card = (input())
    card_list = []
    cardd = card.replace('-', '')

    for i in cardd:
        card_list.append(i)

    if card_list[0] == '3' and len(card_list) == 16:
        print(f'#{t} 1')
    elif card_list[0] == '4' and len(card_list) == 16:
        print(f'#{t} 1')
    elif card_list[0] == '5' and len(card_list) == 16: 
        print(f'#{t} 1') 
    elif card_list[0] == '6' and len(card_list) == 16:
        print(f'#{t} 1')
    elif card_list[0] == '9' and len(card_list) == 16:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')


