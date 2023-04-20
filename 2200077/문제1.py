# 신용카드 번호2

T = int(input())

for t in range(T):
    card_num = input()
    new_card_num = ""
    new_card_num = card_num.replace('-', '')

    if new_card_num[0] in ['3', '4', '5', '6', '9'] and len(new_card_num) == 16:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
