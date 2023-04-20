T = int(input())

for t in range(1, T+1) :
    a = list(input())
    qqq = 0

    if a[0] == '3' or a[0] == '4' or a[0] == '5' or a[0] == '6' or a[0] == '9' :
        for i in a :
            if i == '-' :
                qqq += 1
        if len(a) - qqq == 16 :
            print(f'#{t} 1')
        else :
            print(f'#{t} 0')
    else :
        print(f'#{t} 0')                    