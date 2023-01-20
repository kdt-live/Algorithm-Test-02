T = int(input())

for t in range(1, T+1) :
    li = list(map(int, input().split()))
    new_li = []

    for i in li :
        if li.count(i) != 2 :
            print(f'#{t} {i}')
            break