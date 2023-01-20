# 14649번 - 신용카드 만들기 1
T = int(input())
for tc in range(1, T + 1):
    card = input().split()
    odd, even = 0, 0
    result = 0
    for i in range(0, 15, 2):
        odd += int(card[i]) * 2
    for j in range(1, 15, 2):
        even += int(card[j])
    
    if (odd + even) % 10 == 0:
        result = ((odd + even) % 10)
        print(f'#{tc} {result}')
    else:
        result = ((odd + even) % 10) - 10
        print(f'#{tc} {-result}')