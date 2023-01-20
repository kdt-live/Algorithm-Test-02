# 14649 신용카드 만들기 1


for i in range(1,int(input())+1):
    lst = list(map(int,input().split()))
    card1 = []
    card2 = []
    try:
        for x in range(0,16,2):
            card1.append(lst[x]*2)
            card2.append(lst[x+1])
    except:
        if (sum(card1)+sum(card2))%10 == 0:
            print(f'#{i} 0')
        else:
            print(f'#{i} {10-((sum(card1)+sum(card2))%10)}')
