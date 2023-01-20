T = int(input())

for i in range(1,T+1):
    n = str(input())
    n = n.replace('-','')
    n_able = ['3','4','5','6','9']
    if n[0] in n_able:
        if len(n) ==16:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
    else:
        print(f'#{i} 0')