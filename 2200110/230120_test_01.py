# 신용카드 만들기 2
T = int(input())
card_start = ['3', '4', '5', '6', '9']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for t in range(1, T+1):
    card_ok = input()
    if '-' in card_ok:
        new_card_ok = card_ok.replace("-", "")
    else:
        new_card_ok = card_ok

    for n in new_card_ok:
        if n not in num:
            print(f'#{t} 0')

    if len(card_ok) == 16 + card_ok.count('-'):
        if card_ok[0] in card_start:
            print(f'#{t} 1')

        else:
            print(f'#{t} 0')

    else:
        print(f'#{t} 0')
