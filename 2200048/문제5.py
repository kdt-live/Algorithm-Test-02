# 5
import collections
T = int(input())
for i in range(1,T+1):
    line1 = []
    line = input().split()
    counter = collections.Counter(line)
    for k in counter:
        if counter[f'{k}'] == 1:
            line1.append(k)
    print(f'#{i} {line1[0]}')