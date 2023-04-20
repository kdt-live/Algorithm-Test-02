# Alorithm 1주차 모의고사 230120_14:00~17:30
# 02_SWEA_3456_직사각형길이찾기

import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    abc_len = list(map(int, input().split()))

    for n in abc_len:
        if abc_len[0] != n: # 두수는 같고, 찾는 값은 같지 않은 수 이기때문에 비교해서 다른수를 출력
            print(f'#{test_case} {n}')

    if abc_len[0] == abc_len[1] == abc_len[2]: # 위의 for 문에서 3번돌면 값이 3번 출력되기때문에 if문을 앞으로 뺐습니다.
        print(f'#{test_case} {n}')

# SWEA 결과 Faill ... ㅠㅠ
    