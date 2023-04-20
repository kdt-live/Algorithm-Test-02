t = int(input())
start_n = ['3', '4', '5', '6', '9']

for i in range(t):
    card_n = input().replace('-', '')
    if (card_n[0] in start_n) and (len(card_n) == 16):
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')