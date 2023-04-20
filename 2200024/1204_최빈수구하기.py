from collections import Counter
import sys

T = int(input())

for t in range(1, T+1) :
    n = int(input())    
    li = list(map(int, sys.stdin.readline().split()))

    sorted_li = sorted(li, reverse=True)

    dict_li = Counter(sorted_li).most_common(1)
    print(f'#{t} {dict_li[0][0]}')