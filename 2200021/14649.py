# 신용카드 만들기 1

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    nums = list(map(int,input().split()))
    total = 0
    for i in range(15):
        if i % 2 == 0:
            total += nums[i] * 2   
        else:
            total += nums[i]     
    n = (10 - (total % 10))%10
    print(f'#{t} {n}')
    