T = int(input())

for t in range(1, T+1):
    list = input()
    list = list[::-1]
    result = []
    for i in list:
        if i =='b':
            result +='d'
        elif i == 'd':
            result +='b'
        elif i == 'p':
            result +='q'
        elif i == 'q':
            result +='p'
    print(f'#{t} {result}')