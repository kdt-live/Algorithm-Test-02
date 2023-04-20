t = int(input())
for i in range(1, t+1) :
    n = int(input())
    case = list(map(int,input().split()))
    all_cost = 0
    avg = 0
    cnt = 0
    for x in case :
        all_cost +=x
    avg = all_cost //len(case)
    for y in case :
        if y <=avg :
            cnt +=1
    print(f"#{i} {cnt}")
