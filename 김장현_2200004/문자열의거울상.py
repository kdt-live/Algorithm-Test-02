t = int(input())

for i in range(1, t+1):
    string = input()
    mirror_string = str()
    for index in range(-1, -(len(string)+1), -1):
        if string[index] == 'b':
            mirror_string += 'd'
        if string[index] == 'd':
            mirror_string += 'b'
        if string[index] == 'p':
            mirror_string += 'q'
        if string[index] == 'q':
            mirror_string += 'p'
    print(f'#{i}', mirror_string)