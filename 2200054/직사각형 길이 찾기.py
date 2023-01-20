import sys
input = sys.stdin.readline

TC = int(input())
for t in range(1, TC+1):
    a, b, c = map(int,input().split())
    dict = {}
    for i in [a, b, c]:
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    for i in [a, b, c]:
        if dict[i] == 1:
            print(f'#{t} {i}')
        elif len(dict) == 1:
            print(f'#{t} {a}')
            break

