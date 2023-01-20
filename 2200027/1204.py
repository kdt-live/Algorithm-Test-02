t = int(input())

for i in range(1, t+1):
    case_num = int(input())


    socore = list(map(int,input().split()))
    dic_socore = {}
    for j in range(len(socore)):
        try:
            dic_socore[socore[j]] += 1
        except:
            dic_socore[socore[j]] = 1

    lst_count = sorted(dic_socore.values(), reverse=True)
    print(f'#{i} {sorted(dic_socore.items(), key=lambda x: x[1], reverse=True)[0][0]}')
        
        
