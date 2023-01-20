# 14649
T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    result = 0
    N = list(map(int, input().split()))
    for i in range(len(N)):
        if i % 2 == 1:
            result += N[i]
        else:
            result += N[i] * 2
    
    if result % 10 == 0:  # 10으로 나누었을 때 0이면 16번째 넘버를 0으로 대체
        card_number = 0
    else: 
        card_number = 10 - (result % 10)
    print(f'#{t} {card_number}')