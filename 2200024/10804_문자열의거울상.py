T = int(input())

for t in range(1, T+1) :
    new_li = []
    li = list(input())
    # print(li)
    for i in li :
        if i == 'b' :
            new_li.append('d')
        elif i == 'd' :
            new_li.append('b')
        elif i == 'p' :
            new_li.append('q') 
        else :
            new_li.append('p')
    
    print(f'#{t}', end=" ")        
    print(*new_li[::-1], sep="")
