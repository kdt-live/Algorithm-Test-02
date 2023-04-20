t = int(input())

for i in range(1, t+1):
    card_number = input()
    card_number = card_number.replace('-', '')
    if card_number[0] in ['3', '4', '5', '6', '9']:
        if len(card_number) == 16:
            print(f'#{i}', 1)
        else:
            print(f'#{i}', 0)
    else:
        print(f'#{i}', 0)

