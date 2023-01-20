# 소득 불균형
T=int(input())
for tc in range(T):
    N=int(input())
    incomes=list(map(int,input().split()))
    # 소득합계 초기화
    total=0
    # 평균소득 초기화
    aver=0
    # 카운트 초기화
    cnt=0
    
    for e in incomes:
        total+=e
    aver=total/N
    for i in range(len(incomes)):
        if incomes[i]<=aver:
            cnt+=1
    print(f'#{tc+1} {cnt}')
    pass