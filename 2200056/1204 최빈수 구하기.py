from collections import Counter
T = int(input())

for t in range(1, T+1):
    score_dict = {} # 스코어 딕셔너리 만들기
    result_list = [] # 결과 리스트 만들기
    N = int(input()) 
    score_list = list(map(int, input().split())) # 스코어 리스트 인풋값으로 받아주기
    score_dict = Counter(score_list) # 리스트 중복값들을 딕셔너리로 넣어주는 식
    a = score_dict.most_common(1) # 그중에서 제일 많은 누적값을 변수 a로 설정

    most = a[0][1] # a는 리스트 안에 튜플 형식으로 튜플은 key,value 다 나옴 / 나는 value값만 변수 most에 저장

    for key,value in score_dict.items(): # items로 key와 value 구해주기
        if value == most: # value가 most와 같으면
            result_list.append(key) # result_list에 key 값 추가
    max_result = max(result_list) # result_list의 최댓값 구하기
    print(f"#{t} {max_result}")