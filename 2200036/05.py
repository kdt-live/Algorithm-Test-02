# #14649 신용카드 만들기

T = int(input())
for t in range(1, T + 1):
    card_no = list(map(int, input().split()))
    od_list = []
    ev_list = []
    od_sum = []
    ev_sum = []
    for i in range(len(card_no)):
        if i % 2 == 0:
            od_list.append(card_no[i]) 
        else:
            ev_list.append(card_no[i])
    for o in od_list:
        od_sum.append(o * 2)
    for e in ev_list:
        ev_sum.append(e) 
    total = sum(od_sum) + sum(ev_sum)
    result = (((total // 10) + 1) * 10 - total) % 10
    print(f"#{t} {result}")