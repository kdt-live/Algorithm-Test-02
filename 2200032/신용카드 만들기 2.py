T = int(input())
for test_case in range(1, T+1):
    card = input()
    start = ('3', '4', '5', '6', '9')
    if '-' in card:
        card = card.replace('-', '')
    if len(card) == 16 and card.startswith(start):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')