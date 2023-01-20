# 14649 신용카드 만들기 1


for i in range(1,int(input())+1):
    lst = list(map(int,input().split()))
    card1 = [lst[x]*2 for x in range(0,16,2)]
    card2 = [lst[x] for x in range(1,15,2)]
    n = (sum(card1)+sum(card2)) % 10
    if n == 0:
        print(f'#{i} 0')
    else:
        print(f'#{i} {10-n}')
