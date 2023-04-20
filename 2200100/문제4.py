T = int(input())
cnt = 0
for t in range(T):
    string = input()
    string1 = string[::-1]
    string2 = []
    string3 = ""
    for i in string1:
        if i == 'b':
            string2.append('d')
        elif i == 'd':
            string2.append('b')
        elif i == 'q':
            string2.append('p')
        elif i == 'p':
            string2.append('q')
        cnt += 1
    for k in string2:
        string3 += k
    print(f'#{t+1} {string3}')
    string2 = []
    string3 = ""
