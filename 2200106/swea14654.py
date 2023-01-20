t = int(input())
for tc in range(1, t+1):
    cards = input()
    del_hyphen = [i for i in cards if i != '-']
    #print(del_hyphen)

    if del_hyphen[0] in ['3', '4', '5', '6', '9'] and len(del_hyphen) == 16:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')