# 직사각형 길이 찾기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    li = list(map(int,input().split()))
    for i in li:
        if li.count(i) == 1 or li.count(i) == 3:
            print(f'#{t} {i}')
            break