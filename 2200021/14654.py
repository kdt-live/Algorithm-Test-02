# 신용카드 만들기 2

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    s = input()
    li = ['3','4','5','6','9']
    for i in s:
        s = s.replace('-','')
    if s[0] in li and len(s.strip()) == 16:
        is_card = True
    else:
        is_card = False
    print(f'#{t} {int(is_card)}')
    