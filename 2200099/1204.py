import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    case = int(input())
    Number = list(map(int, input().split()))
    tmp = {}
    for n in Number:
        try:
            tmp[n] += 1
        except:
            tmp[n] = 1
    tmp_sort = sorted(tmp.items(), key=lambda item:item[1], reverse=True)
    for x, b in tmp_sort:
        if b == min(tmp_sort[0]):
            print(f'#{case} {x}')
            break
    