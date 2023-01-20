# b, d, p, q로 이루어진 문자열이 주어진다 이 문자열을 거울에 비추면 어떤 문자열이 되는지를 구하는 프로그램을 구하여라
# 입력 : 첫번째 줄에 테스트 케이스의 수 T가 주어진다.
# 출력 : 각 테스트 케이스마다 주어진 문자열을 거울에 비춘 문자열로 출력한다.

T = int(input())

for t in range(T):
    S = input()
    result = []
    for s in S[::-1]:
        if s == 'd':
            result.append('b')
        elif s == 'b':
            result.append('d')
        elif s == 'p':
            result.append('q')
        elif s == 'q':
            result.append('p')

    print(f'#{t+1} ', *result, sep='')