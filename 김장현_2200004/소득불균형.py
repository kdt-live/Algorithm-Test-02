t = int(input())

for i in range(1, t+1):
    people_num = int(input())
    people_income = list(map(int, input().split()))
    average_income = sum(people_income)/people_num
    cnt = 0 

    for people in people_income:
        if people <= average_income:
            cnt += 1
    
    print(f'#{i}', cnt)