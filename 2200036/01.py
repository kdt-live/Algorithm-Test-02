#1204 최빈수 구하기

T = int(input())
for t in (1, T + 1): # 테스트 케이스
    a = int(input()) # 케이스 회차
    score = list(map(int,input().split())) #점수 목록
    score_cnt = {} # 딕셔너리 생성
    for i in score: 
        if i in score_cnt: # 점수가 딕셔너리에 있다면
            score_cnt[i] += 1 #카운트 추가
        else:              # 점수가 딕셔너리에 새로 들어가는 거면
            score_cnt[i] = 1 # 1 입력
        
    freq = max(score_cnt.values()) # 가장 자주 나온 점수의 회수
    max_cnt = 0 # 최대 출현수가 나온 회수
    score_list = list(score_cnt.keys())
    count_list = list(score_cnt.values())
    for k, v in count_list: # 점수 목록을 돌면서
        if v == freq:
            max_cnt += 1
    
        if max_cnt >= 2:
            alevel =
            print(alevel)


            
        
        

