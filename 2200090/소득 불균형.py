for t in range(1, int(input())+1):
    n = int(input())
    number = list(map(int, input().split()))
    avg_ = sum(number) // len(number)
    cnt = 0
    for i in number:
        if i <= avg_:
            cnt += 1
    print(f'#{t} {cnt}')