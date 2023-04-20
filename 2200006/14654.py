# 14654번 - 신용카드 만들기 2
T = int(input())
first_num = ['3', '4', '5', '6', '9']
for tc in range(1, T + 1):
    card = input()
    if card[0] in first_num and (len(card) == 16 or len(card) == 19):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')