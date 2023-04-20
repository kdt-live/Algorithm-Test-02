for t in range(1, int(input())+1):
    card = input()
    card = ''.join(list(card.split('-')))
    if card[0] in '34569' and len(card) == 16:
        n = 1 
    else:
        n = 0
    print(f'#{t} {n}')