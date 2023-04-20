#14654
T = int(input())

for t in range(1, T+1):
    card = input()      # len을 위해 str로 받았다.
    if "-" in card:     # -를 뺀다
        card = card.replace("-", "")
    if len(card) == 16:
        if int(card[0:1]) in [3, 4, 5, 6, 9]:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    else:
        print(f'#{t} 0')