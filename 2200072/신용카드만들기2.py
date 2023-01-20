T = int(input())
start_numbers = ['3','4','5','6','9']
for i in range(T):
  card_numbers = input().split('-')

  if len(card_numbers) == 1:
    if len(list(card_numbers[0])) == 16 and list(card_numbers)[0][0] in start_numbers:
      print(f'#{i+1} 1')
    else:
      print(f'#{i+1} 0')
  elif len(card_numbers) == 4:
    if card_numbers[0][0] in start_numbers:
      print(f'#{i+1} 1')
    else:
      print(f'#{i+1} 0')
  else:
    print(f'#{i+1} 0')

