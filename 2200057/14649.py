T = int(input())

for t in range(1, T+1):
    li = list(map(int, input().split()))
    result = 0
    for i in range(15):
        if i % 2:
            result += li[i]
        else:
            result += 2 * li[i]
    print(f'#{t} {(10 - (result % 10)) % 10}')