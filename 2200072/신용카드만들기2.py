T = int(input())
start_numbers = ['3','4','5','6','9']
for i in range(T):
  card_numbers = input()

  card_numbers_list = list(card_numbers.replace('-',''))

  if len(card_numbers_list) == 16 and (card_numbers_list[0] in start_numbers):
    print(f'#{i+1} 1')
  else:
    print(f'#{i+1} 0')

