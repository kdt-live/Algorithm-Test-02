import sys
sys.stdin = open('input_1204.txt', 'r')
'''
## 제출한 답
from collections import Counter # 라이브러리 사용

T = int(input())

for _ in range(T):
    t = int(input()) # 테스트 케이스 번호
    a = Counter(input().split()) # Counter 사용

    # 큰 점수부터 나열 # 튜플로 바뀐다
    a = sorted(a.items(), reverse=True)
    # 최빈수
    a = sorted(a, key = lambda x: x[1], reverse=True)
    print(f'#{t} {a[0][0]}')

'''
'''
## Counter 없이

T = int(input())

for _ in range(T):
    t = int(input()) # 테스트 케이스 번호
    a = input().split()

    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1

    # 큰 점수부터 나열 # 튜플로 바뀐다
    d = sorted(d.items(), reverse=True)
    # 최빈수
    d = sorted(d, key = lambda x: x[1], reverse=True)
    print(f'#{t} {d[0][0]}')
'''


# 다중조건 정렬

T = int(input())

for _ in range(T):
    t = int(input()) # 테스트 케이스 번호
    a = list(map(int, input().split()))

    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1

    # 다중조건 정렬
    d = sorted(d.items(), key = lambda x: (-x[1], -x[0]))
    print(f'#{t} {d[0][0]}')