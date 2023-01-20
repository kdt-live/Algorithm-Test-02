t = int(input())
for tc in range(1, t+1):
    
    squre = list(map(int, input().split()))
    if squre.count(squre[0]) == 3:
        print(f'#{tc} {squre[0]}')
    else:
        for ele in squre:
            if squre.count(ele) == 1:
                print(f'#{tc} {ele}')