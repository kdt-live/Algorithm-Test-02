T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    pay = list(map(int, input().split()))
    print(f'#{test_case} {len(list(filter(lambda x:x<=sum(pay)/n, pay)))}')