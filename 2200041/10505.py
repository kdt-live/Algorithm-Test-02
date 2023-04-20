#10505
# T, 사람, 소득, 평균, 저소득(초기화)
# 평균보다 작은 사람구함

T = int(input())

for t in range(1, T+1):
    low_pay = 0
    peope = int(input())
    pay = list(map(int, input().split()))
    avg = sum(pay) // peope
    
    for P in pay:
        if P <= avg:
            low_pay += 1
    
    print(f'#{t} {low_pay}')
