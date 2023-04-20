# qppdb
# pqqbd

T = int(input())

for i in range(1,T+1):
    t_c = str(input())
    t_c_0 = t_c[::-1]
    t_c_1 = ''
    for j in t_c_0:
        if j == 'q':
            t_c_1 += 'p'
        elif j == 'p':
            t_c_1 += 'q'
        elif j == 'd':
            t_c_1 += 'b'
        elif j =='b':
            t_c_1 += 'd'
    print(f'#{i} {t_c_1}')    