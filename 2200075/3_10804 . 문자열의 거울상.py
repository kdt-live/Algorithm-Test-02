# 3. 
T = int(input())

for t in range(1,T + 1) :
    result = input()[::-1]
    print(f'#{t} ',end='')
    for i in result :
        if i == 'q':
            print('p',end='')
        elif i == 'p':
            print('q',end='')
        elif i == 'b':
            print('d',end='')
        elif i == 'd':
            print('b',end='')
    print()