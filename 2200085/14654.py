T = int(input())

for t in range (T):
    credit = input()
    if '-' in credit:
        credit = credit.replace('-', '')

    if (len(credit) != 16):
        result = 0
        print(f'#{t+1} {result}')
        continue
    
    if (credit[0] not in '34569'):
        result = 0
        print(f'#{t+1} {result}')
        continue

    else:
        result = 1

    print(f'#{t+1} {result}')