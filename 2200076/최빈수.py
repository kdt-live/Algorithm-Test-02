t = int(input())
for i in range(t):
    turn = int(input())
    score = list(map(int, input().split()))
    score_cnt = {}
    for s in score:
        if s in score_cnt:
            score_cnt[s] += 1
        else:
            score_cnt[s] = 1

    rank = sorted(score_cnt.items(), key=lambda x: x[1], reverse=True)
    
    cnt = 0   # 최빈수와 같은 값이 몇개인지 카운트
    while rank[cnt][1] == rank[cnt+1][1]:
        cnt += 1
    
    if cnt == 0:
        print(f'#{turn} {rank[0][0]}')
    else:
        big_n = 0
        for i in range(cnt+1):
            if rank[i][0] > big_n:
                big_n = rank[i][0]
        print(f'#{turn} {big_n}')
