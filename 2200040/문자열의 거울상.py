import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
# 케이스 수

for t in range(1, T+1):
    ts = input()
    ts = list(reversed(ts))
    cnt = 0
    for i in ts:
        if i =='q':
            ts[cnt] = 'p'
            cnt += 1
        elif i == 'p':
            ts[cnt] ='q'
            cnt += 1
        elif i == 'd':
            ts[cnt] = 'b'
            cnt += 1
        elif i == 'b':
            ts[cnt] = 'd'
            cnt += 1
    ans = ''.join(ts)
    print(f'#{t} {ans}')
# b d p q로 이루어진 문자열을 순서를 뒤집고 q->p  / p -> q / d -> b / b -> d
