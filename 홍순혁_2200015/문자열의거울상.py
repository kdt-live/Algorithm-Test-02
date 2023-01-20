a = int(input())

for i in range(1,a+1):
    c=[]
    b = list(input())
    for j in b:
        if j =='q':
            c.append('p')
        if j =='p':
            c.append('q')
        if j =='b':
            c.append('d')
        if j =='d':
            c.append('b')
    c.reverse()
    d = ''.join(map(str,c))
    print(f'#{i} {d}')



