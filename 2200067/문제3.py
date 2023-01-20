'''
소득 불균형
'''
T= int(input())
for _ in range(1,T+1):
    n = int(input())
    income = list(map(int,input().split()))
    income_avg = sum(income)/n

    cnt = 0
    for i in income:
        if i <= income_avg:
            cnt += 1
    print(f'#{_} {cnt}')

 