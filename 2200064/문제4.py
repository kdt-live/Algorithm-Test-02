# 문자열의 거울상

T = int(input())

for tc in range(1, T+1):
    string = list(input())
    mirror = {'b':'d', 'd':'b', 'q':'p', 'p':'q'}
    result = ''
    string.reverse()
    for i in string:
        result += mirror[i]
    print(f'#{tc} {result}')