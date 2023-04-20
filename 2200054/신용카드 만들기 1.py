# 1) 매 홀수자리의 숫자마다 2를 곱해서 더합니다. 
# 2) 매 짝수자리의 숫자는 그대로 더합니다.
# 3) 1)과 2)를 더 한 숫자에 N을 더 한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효한 숫자입니다. 

import sys
input = sys.stdin.readline

TC = int(input())
for t in range(1, TC+1):
    numberlist = list(map(int, input().split()))
    nsum1 = 0 # 홀수 자리의 합
    nsum2 = 0 # 짝수 자리의 합
    for i in range(1, len(numberlist)+1):
        if i % 2 >= 1: # 홀수자리
            nsum1 += numberlist[i-1]*2
        elif i % 2 == 0:
            nsum2 += numberlist[i-1]
    answer = 10 - (nsum1 + nsum2) % 10
    # print(nsum1)
    # print(nsum2)
    # print(nsum1+nsum2)
    if answer == 10: answer = 0
    print(f'#{t} {answer}')
