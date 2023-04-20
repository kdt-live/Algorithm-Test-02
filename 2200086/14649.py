# 신용카드 만들기 1

T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    result = 0
    cnt = 1
    while cnt < 16:
        if cnt % 2 == 1:
            result += num[(cnt-1)]*2
            cnt += 1
        else:
            result += num[(cnt-1)]
            cnt += 1
    if result % 10 == 0:
        print(f'#{t}', 0)
    else:
        print(f'#{t}', 10 - (result % 10))