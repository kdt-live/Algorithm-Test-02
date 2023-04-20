t = int(input())
for tc in range(1, t+1):
    cards = list(map(int, input().split()))
    sum = 0
    #print(cards)

    
    for i in range(len(cards)):
        if i % 2 == 0:
            sum += cards[i] * 2
        else:
            sum += cards[i]
    #print(sum)

    if sum % 10 == 0:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {10 - sum%10}')