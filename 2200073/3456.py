import sys
sys.stdin = open('input_3456.txt', 'r')

## 제출한 답
T = int(input())

for t in range(1, T+1):
    d = {}
    a = list(map(int, input().split()))
    for i in a:
        d[i] = d.get(i,0) +1
    for k, v in d.items():
        if v == 1 or v == 3:
            print(f'#{t} {k}') # k가 문자형일때 틀렸다고 뜬다!