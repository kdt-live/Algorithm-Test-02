#최빈수 구하기
from collections import Counter
T = int(input())
for i in range(1,T+1):
    n = int(input())
    count = Counter(list(map(int,input().split())))
    print(f'#{i} {count.most_common(1)[0][0]}')