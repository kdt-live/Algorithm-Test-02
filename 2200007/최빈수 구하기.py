import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range (1, T+1) :
    n = int(input())
    N = list(map(int,input().split()))
    max_num = 0

    for i in N :
        if N.count(i) == 0 :
            continue
        elif N.count(i) >= N.count(max_num) :
            max_num = i
    print(f"#{t} {max_num}")