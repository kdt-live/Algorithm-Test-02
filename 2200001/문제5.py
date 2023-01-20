# 신용카드 만들기 1
T = int(input())

for t in range(1, T+1):
    card = list(map(int, input().split()))
    num = 0
    num1 = 0

    for i in range(len(card)):
        if (i+1) % 2 == 1:
            num += int(card[i]) * 2
        else:
            num1 += int(card[i])
    
    total = num + num1

    if total % 10 != 0:
        a = total % 10
        result = 10 - a
    else :
        result = 0

    print(f'#{t} {result}')