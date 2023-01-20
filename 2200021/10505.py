# 소득 불균형

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    n = int(input())
    nums = list(map(int,input().split()))
    average = sum(nums)//n
    cnt = 0
    for i in nums:
        if i <= average:
            cnt += 1
    print(f'#{t} {cnt}')