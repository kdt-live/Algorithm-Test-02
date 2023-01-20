# Alorithm 1주차 모의고사 230120_14:00~17:30
# 04_SWEA_10804_문자열의거울상.py

import sys
sys.stdin = open("input4.txt", "r")

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1):
    String = input() # 글자를 입력받습니다.
    result_list = []
    for s in String:
        if s == 'b':
            result_list.append('d') # b는 d로 바꾸어서 리스트에 넣어줍니다
        elif s == 'd':
            result_list.append('b') # d는 b로 바꾸어서 리스트에 넣어줍니다
        elif s == 'p':
            result_list.append('q') # p는 q로 바꾸어서 리스트에 넣어줍니다
        else :
            result_list.append('p') # 나머지 q는 p에 넣어줍니다

    result = ''.join(map(str, result_list)) # 리스트의 값은 result에 넣어 주면서 중간에 간격(' '->'')을 없애줍니다.
    print(f'#{test_case} {result[::-1]}') # 형식에 맞게 출력합니다.

# 처음에 간단하네? 하면서 신나게 역순으로 정렬했더니... 글자 자체가 바뀐거였더군요..
# 또 신나게 글자를 바꿨더니 ... 잉? ... 바꾼후에  또 역순 ㅠㅠㅠㅠ
    