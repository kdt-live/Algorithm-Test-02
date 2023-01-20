t = int(input())
for i in range(t):
    string = reversed(list(input()))
    print(f'#{i+1} ', end='')
    for s in string:
        if s == 'b':
            print('d', end='')
        elif s == 'd':
            print('b', end='')
        elif s == 'p':
            print('q', end='')
        elif s == 'q':
            print('p', end='')
    print()