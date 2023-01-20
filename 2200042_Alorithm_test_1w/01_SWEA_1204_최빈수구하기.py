# Alorithm 1주차 모의고사 230120_14:00~17:30
# 01_SWEA_1204_최빈수구하기.py

import sys
sys.stdin = open("input1.txt", "r")

T = int(input()) # 전체 테스트 케이스 수
Number_dict = {}
Mumbers = []

for test_case in range(1, T + 1):
    N = int(input()) # 각각의 테스트 케이스 수
    Numbers = list(map(int, input().split()))
    Number_dict[N] = Numbers

for key, value in Number_dict.items():
    # print(key)

# print(Number_dict)

# 다 못풀었습니다 ㅠㅠ
# .... 아 ... 틀린 코드 지워버렸네요 ㅠㅠㅠ 너무 아닌것같아서 다시하려고 지웠는데 ㅠㅠㅠ
# 어제 실습에 이와 유사한 문제 나왔을때도 못풀어서 다 지우고 올렸었는데 .... ㅠㅠ
# 다음에는 주석처리하고 해보도록 하겠숩니다.