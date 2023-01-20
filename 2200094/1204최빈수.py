
# import sys
# sys.stdin = open('input (4).txt')


# 점수와 빈도수를 세트로 만들어 제일 큰 값만 출력



T  = int(input())

for t in range(1, T+1):
    testcase = int(input())
    scores = list(map(int, input().split())) # txt파일 불러와서 빨리 입력하는 법 기억이 안남 ㅜㅜ
    result = 0  # 출력할 최빈수 변수 / 근데 딕셔너리로 만들거니깐 key 값을 할당해줄것이다.

    dic = {} # (숫자 : 빈도수) 형태로 딕셔너리 만들기
    for i in scores: # 점수를 하나씩 꺼내서
        if i not in dic:     # 딕셔너리에 없으면(첫출현이라면)
            dic[i] = 1    # 키생성, 값은 1로  // 딕셔너리[key] = value 형태로 삽입한다. 없으면 수정도 함
        else:
            dic[i] += 1   # 딕셔너리에 이미 생성되어있는 점수라면 값(빈도수) 1씩 더하기


    count = 0  # 
    for key, value in dic.items():
        if count < value:
            count = value # 할당시켜줌
     # 그리고는 막혓습니다..