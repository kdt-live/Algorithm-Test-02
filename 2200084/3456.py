T = int(input())
for i in range(1, T+1):
    squ = list(map(int, input().split()))
    for j in squ:
        if squ.count(j) % 2 == 1:
            print(f'#{i} {j}')
            break