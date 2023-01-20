# 10804 문자열의 거울상
text = ['b','p','d','q']
mirror = ['d','q','b','p']

for i in range(1,int(input())+1):
    n = list(input()[::-1])
    m = []
    for x in n:
        m.append(mirror[text.index(x)])
    print(f'#{i} {"".join(m)}')
