import sys
sys.stdin = open('input_10804.txt', 'r')


# 제출한 답
data = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',
}
T = int(input())
for t in range(1, T+1):
    result = ''
    for i in input()[::-1]:
        result += data[i]
    print(f'#{t} {result}')
