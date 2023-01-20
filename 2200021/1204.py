# 1일차 - 최빈수 구하기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


for t in range(int(input())):
    t_c = int(input())
    max_li = 0
    li = list(map(int,input().split()))
    for i in range(101):
        if li.count(i) >= max_li:
            max_li = li.count(i)
            max_i = i
    print(f'#{t_c} {max_i}')