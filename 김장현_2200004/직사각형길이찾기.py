t = int(input())

for i in range(1, t+1):
    a = list(map(int, input().split()))
    for side in a:
        if a.count(side) in [1]:
            print(f'#{i}', side)
        if a.count(side) in [3]:
            print(f'#{i}', side) 
            break