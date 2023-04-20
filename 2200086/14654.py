# 신용카드 만들기 2
T = int(input())
for i in range(1, T+1):
    N = input()
    li = []
    if N[0] in '34569':
        for j in N:
            if j != '-':
                li.append(j)
    
    if len(li) == 16:
        print(f'#{i}', 1)
    else:
        print(f'#{i}', 0)
