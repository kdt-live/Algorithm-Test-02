T = int(input())
bdpq_rvs = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}
for i in range(1, T+1):
    bdpq = input()
    bdpq_lst = []
    for j in bdpq:
        j = bdpq_rvs[j]
        bdpq_lst.append(j)
    bdpq_lst.reverse()
    print(f'#{i} ', *bdpq_lst, sep='')