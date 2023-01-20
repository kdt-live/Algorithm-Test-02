T = int(input())
for t in range(1, T+1):
    string = input()
    tmp_string = ''
    for i in string:
        if i == 'd':
            tmp_string = 'b'+tmp_string
        elif i == 'b':
            tmp_string = 'd'+tmp_string
        elif i == 'p':
            tmp_string = 'q'+ tmp_string
        elif i == 'q':
            tmp_string = 'p'+tmp_string
    print(f'#{t} {tmp_string}')