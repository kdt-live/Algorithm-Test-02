# 문자열의 거울상

T = int(input())
for i in range(1, T+1):
    a = input()
    li = []
    li2 = []    
    for j in a:
        if j == 'b':
            li.append('d')
        elif j == 'd':
            li.append('b')
        elif j == 'p':
            li.append('q')
        elif j == 'q':
            li.append('p')
    for m in li[::-1]:
        li2.append(m)
    b = ''.join(li2)
    print(f'#{i}', b)