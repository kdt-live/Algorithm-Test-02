# 신용카드 만들기

import sys
sys.stdin = open("input_14649.txt")

T = int(input())

for i in range(T):
    ls = list(map(int, input().split()))
    
    odd = sum(map(lambda x: x * 2, ls[::2]))
    even = sum(ls[1::2])
    
    N = (odd + even) % 10
    print(f"#{i + 1} {(10 - N) % 10}")