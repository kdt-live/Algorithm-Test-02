# 14654. 신용카드 만들기 2

for i in range(1,int(input())+1):
    card = list(input())
    for j in card:
        if j == '-':
            card.remove(j)
    if len(card) == 16 and card[0] in ['3', '4', '5', '6', '9']:
        print(f'#{i}', '1')
    else:
        print(f'#{i}', '0')