T = int(input())

for i in range(T):
    num = list(input())
    card = []

    if num[0] == '3' or num[0] == '4' or num[0] == '5' or num[0] == '6' or num[0] == '9':

        for j in range(len(num)):
            if num[j] == '-':
                pass
            else:
                card.append(num[j])
        
        if len(card) == 16:
            print(f'#{i+1} 1')
            card = []
        else:
            print(f'#{i+1} 0')
            card = []

    else:
        print(f'#{i+1} 0')