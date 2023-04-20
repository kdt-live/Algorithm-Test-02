# import sys
# sys.stdin = open('input.txt','r')

T = int(input())

cnt = 0

for t in range(1,T+1):
    x = 0
    num = list(map(int,input().split()))
    for i in num:
        if i % 2 == 0:
            x +=(i*2)
        else:
            x += i

        if x % 10 != 0:
            x += 1
            cnt += 1
        else:
            break

print(cnt)