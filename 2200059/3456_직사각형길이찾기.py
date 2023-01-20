# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b:
        answer = c
    elif b == c:
        answer = a
    elif c == a:
        answer = b
    print(f'#{t} {answer}')
