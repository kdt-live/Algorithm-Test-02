# Alorithm 1주차 모의고사 230120_14:00~17:30
# 05_SWEA_14649_신용카드만들기.py

import sys
sys.stdin = open("/Users/mi23/Desktop/Alorithm_test_1w/input5.txt", "r")

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T + 1):
    number_list = list(map(int, input().split())) # 카드번호 15자리를 리스트에 저장합니다.
    odd = 0 # 홀수값에 2를 곱한 값
    even = 0 # 짝수들을 더한 값
    result = 0 # 홀수 짝수의 데이터를 더한 값
    N = 0 # 룬 공식(카드번호에서 마지막자리(열여섯번째)숫자

    for n in number_list:
        if n%2 == 1: # 홀수라면
            odd += n*2 # 2를 곱해서 더해줍니다.
        elif n%2 == 0: # 짝수라면
            even += n # 그 값을 그대로 더해 줍니다.
    result = odd + even

    while True:
        if result%10 != 0: # 10으로 나누었을때 0이 아니면 +1
            N += 1
        if result%10 == 0: # 0으로 나누어지면 break
            break
    # 아무래도 while 문이 잘못 된것 같습니다 ㅠㅠㅠ

    print(f'#{test_case} {N}')

