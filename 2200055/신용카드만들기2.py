T=int(input())
for i in range (1,T+1):
    c_num=input()
    if c_num[0] not in ['3','4','5','6','9']:
        print(f'#{i} 0')
    else:
        if len(c_num.replace('-',''))!=16:
            print(f'#{i} 0') 
        else:
            print(f'#{i} 1')