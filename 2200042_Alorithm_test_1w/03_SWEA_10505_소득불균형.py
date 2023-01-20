# Alorithm 1주차 모의고사 230120_14:00~17:30
# 03_SWEA_10505_소득불균형.py
import sys
sys.stdin = open("input3.txt", "r")

T = int(input()) # 전체 테스트 케이스 수

for test_case in range(1, T+1):
    N = int(input()) # 각각의 테스트 케이스 수
    Numbers = list(map(int, input().split()))
    num_sum = 0 # 소득의 합
    result = 0 # 평균이하의 소득을 가진 사람들

    for n in Numbers:
        num_sum += n # 소득의 합 계산
    average = num_sum/N # 소득의 평균

    for n in Numbers:
        if n <= average: # 평균 이하일 경우
            result += 1 # 1을 더한다

    print(f'#{test_case} {result}')
    
# 16:06 ... 드디어 한 문제 합격 ㅠㅠ