# 문제 3 : 문자열의 거울상
T = int(input())

for t in range(1, T+1):
    s = input()
    text = ''
    for i in s[::-1]:
        if i == 'b':
            text += 'd'
        elif i == 'd':
            text += 'b'
        elif i == 'p':
            text +='q'
        else:
            text += 'p'
    print(f'#{t} {text}')