T = int(input())
for test_case in range(1, T + 1):
    card_num = input()
    answer = 0
    if (card_num[0] in ['3', '4', '5', '6', '9']) and (len(''.join(card_num.split('-'))) == 16):
        answer = 1
    print(f'#{test_case} {answer}')