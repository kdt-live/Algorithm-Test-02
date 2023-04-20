'''
최빈수 구하기
'''
# import sys
# sys.stdin = open('input.txt')

T = int(input())
for _ in range(1,T+1):
    
    n = int(input())
    score = list(map(int, input().split()))
    max_cnt = 0

    for i in range(101):
        if score.count(i) == 0:
            continue
        elif score.count(i) >= score.count(max_cnt):
            max_cnt = i
             
    print('#{} {}'.format(n, max_cnt))


