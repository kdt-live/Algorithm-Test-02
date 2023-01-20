t = int(input())

for i in range(t):
    total = 0
    card_n = list(map(int, input().split()))
    
    for index, n in enumerate(card_n):
        if index+1 & 1:  # 홀수 자리일 경우 곱하기2
            total += n*2
        else:
            total += n
    
    last_n = 10 - total%10
    print(f'#{i+1} {last_n%10}')