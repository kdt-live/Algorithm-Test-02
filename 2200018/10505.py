# 소득 불균형

import sys
from math import ceil

sys.stdin = open("input_10505.txt")

T = int(input())

for i in range(T):
    n = int(input())
    ls = list(map(int, input().split()))
    ls = list(map(lambda x: ceil(max(x - sum(ls)/n, 0)), ls))

    print(f"#{i + 1} {ls.count(0)}")
