t=int(input())
for i in range(1,t+1):
    N=int(input())
    income=list(map(int,input().split()))
    avg=sum(income)/N
    low_income=0
    for person in income:
        if person<=avg:
            low_income+=1
    print(f'#{i} {low_income}')