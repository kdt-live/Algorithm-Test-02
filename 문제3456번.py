sol=[]
for T in range(int(input())) :
    a, b, c = input().split(sep=' ')
    if a==b :
        x = c
    elif b==c :
        x = a
    else :
        x = b
    sol.append('#{} {}'.format(T+1, x))
print('\n'.join(sol))