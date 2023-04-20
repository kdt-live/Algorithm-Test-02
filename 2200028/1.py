import sys
sys.stdin = open("예제입력.txt", "r")

T = int(input())
for t in range(1, T+1):
    list = ['3','4','5','6','9']
    card = input()
    if len(card) == 16 or len(card) == 19:
        if card[0] in list:
            print(f'#{t} {1}')
        else:
            print(f'#{t} {0}')
    else:
        print(f'#{t} {0}')