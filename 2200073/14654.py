import sys
sys.stdin = open('input_14654.txt', 'r')

# 제출한 답
T = int(input())

for t in range(1, T+1):
    check = 1
    a = input().replace('-','')
    if len(a) != 16 or a[0] not in ['3','4','5','6','9']: # ['3','4','5','6'] 으로도 통과 했다?!
        check = 0

    print(f'#{t} {check}')