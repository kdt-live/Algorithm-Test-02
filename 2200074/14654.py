T = int(input())
start_num = [3, 4, 5, 6, 9]

for test_case in range(1, T + 1):
    input_numbers = input().replace('-','')

    card_numbers = list(map(int, input_numbers))
    result = 1 if len(card_numbers) == 16 and card_numbers[0] in start_num else 0
    
    print(f'#{test_case} {result}')