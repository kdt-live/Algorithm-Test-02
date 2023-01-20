T = int(input())
for i in range(1, T+1):
    card_num = list(map(int, input().split()))
    sum_card = 0
    for j in range(len(card_num)):
        if j % 2 == 0:
            sum_card += card_num[j]*2
        else:
            sum_card += card_num[j]
    if sum_card % 10 == 0:
        print(f'#{i} {(sum_card % 10)}')
    else:
        print(f'#{i} {10 - (sum_card % 10)}') 