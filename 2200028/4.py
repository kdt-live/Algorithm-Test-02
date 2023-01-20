import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for t in range(1, T+1):
    N = 2
    for _ in range(2):
        avg = 0
        num_list= list(map(int,input().split()))
        result = []
        avg = sum(num_list)/len(num_list)
        for i in num_list:
            if i <= avg:
                result.append(i)
    print(f'#{t} {len(result)}')