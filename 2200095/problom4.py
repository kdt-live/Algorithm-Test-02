# 10804. 문자열의 거울상
T = int(input())
for t in range(T):
    input_list = list(input())
    input_list.reverse()
    res = []
    for key in input_list:
        if key == 'b':
            res.append('d')
        if key == 'd':
            res.append('b')
        if key == 'q':
            res.append('p')
        if key == 'p':
            res.append('q')
    print(f'#{t+1}', end=' ')
    print(*res, sep='',end='\n')
    
    

