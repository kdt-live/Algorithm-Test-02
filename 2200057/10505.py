T = int(input())
for t in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    avg = sum(li) / n
    ans = list(filter(lambda x: x <= avg, li))
    print(f'#{t} {len(ans)}')
