# 문제 1 : 신용카드 만들기 2 

T = int(input())
start_number = ['3', '4', '5', '6', '9']

for t in range(1, T+1):
    card = input().split()
    for i in card:
        if i[0] not in start_number:
            print(f'#{t} 0')
        else:
            print(f'#{t} 1')