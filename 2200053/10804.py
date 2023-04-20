# 문자열의 거울상
T = int(input())

for t in range(1, T+1):
    string = list(input())
    string.reverse()
    for i in range(len(string)):
        if string[i] == 'b':
            string[i] = 'd'
        elif string[i] == 'd':
            string[i] = 'b'
        elif string[i] == 'p':
            string[i] = 'q'
        elif string[i] == 'q':
            string[i] = 'p'

    print(f'#{t}', ''.join(string))