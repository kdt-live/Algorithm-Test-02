T = int(input())
for t in range(1, T+1):
    rec = list(map(int, input().split()))
    for i in rec:
        if rec.count(i) == 1 or rec.count(i) == 3:
            left_one = i

    print(f'#{t} {left_one}')
