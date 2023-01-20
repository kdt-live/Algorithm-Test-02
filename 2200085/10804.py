T = int(input())

for t in range (T):
    string = input()
    string_reverse = ''
    
    for alph in string[::-1]:
        if alph == 'b':
            string_reverse += 'd'

        elif alph == 'd':
            string_reverse += 'b'

        elif alph == 'p':
            string_reverse += 'q'

        else:
            string_reverse += 'p'
    
    print(f'#{t+1} {string_reverse}')