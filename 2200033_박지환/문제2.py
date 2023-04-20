# 신용카드 만들기 1

T = int(input())

card_list = [list(map(int, input().split())) for i in range(T)]


for i in range(T):
    sum = 0
    for j in range(len(card_list[i])): 
        if (j+1) % 2 == 1: # 카드 리스트의 홀수 번째는 2 곱해서 더함
            sum += card_list[i][j]*2
        elif (j+1) % 2 == 0:  # 카드 리스트의 짝수 번째는 그대로 더함
            sum += card_list[i][j]

    print(f'#{i+1} {abs((sum % 10)-10)%10}') # 다 더한 값을 1. 10으로 나눈 나머지에 
                                                         # 2. 10을 빼고 
                                                         # 3. 절대값을 취한 다음 
                                                         # 4. 10으로 나눈 나머지 -> 10을 0으로 바꾸기 위함


