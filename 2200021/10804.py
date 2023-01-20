# 문자열의 거울상

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    s = input()[::-1].strip()
    before = 'bdpq'
    after = 'dbqp'
    tr = str.maketrans(before,after)
    print(f'#{t} {s.translate(tr)}')


