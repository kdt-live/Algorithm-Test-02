t = int(input())

for i in range(1, t+1):
    case_num = int(input())
    socore = list(map(int,input().split()))
    answer = {}
    for j in range(len(socore)):
        try:
            answer[socore[j]] += 1
        except:
            answer[socore[j]] = 1
    count_list = sorted(answer.values(), reverse=True) #카운트수 역순으로 정렬

    if count_list[0] == count_list[1]: #최빈값 중복되면
        max_num = sorted(answer.keys(), reverse=True)[0]
        print(f'#{i} {max_num}')
    else:
        for k, v in answer.items():
            if v == count_list[0]:
                print(f'#{i} {k}')
            
