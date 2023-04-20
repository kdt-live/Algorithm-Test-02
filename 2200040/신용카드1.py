# 1. 매 홀수자리의 숫자마다 2를 곱해서 더한다.
# 2. 매 짝수 자리의 숫자는 그대로 더한다.
# 1과2를 더 한 숫자에 N을 더한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효한 숫자이다
# 16자리 중 15자리가 주어지고 마지막 숫자 N을 구하는 것



import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    odd_number = 0
    even_number = 0
    cnt =1
# 홀수 자리 수 조건
    for j in numbers:
        if cnt%2 ==1 :
            odd_number += (j*2)
            cnt += 1
# 짝수 자리수 조건
        elif cnt%2 ==0:
            even_number += j
            cnt += 1
# 1과 2를 더한 값
    sum_number = odd_number + even_number
    print(sum_number)
# 0부터 1까지 대입할 값
    for i in range(10):
        if (sum_number+i)%10 == 0:
            print(f"#{t} {i}")
# ((1+2)+N %10) == 0
# N을 0부터 9까지 대입해서 %10 == 0이 되는 값을 찾는다.