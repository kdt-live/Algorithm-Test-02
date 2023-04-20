# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    string = input()
    new_string = ''
    for i in string[::-1]:
        if i == 'q':
            new_string += 'p'
        elif i == 'p':
            new_string += 'q'
        elif i == 'd':
            new_string += 'b'
        elif i == 'b':
            new_string += 'd'
    print(f'#{t} {new_string}')
