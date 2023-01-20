T = int(input())

for t in range (1, T+1) :
    S = input()
    S_rev = ''
    ans = ''

    for s in S :
        S_rev = s + S_rev

    for i in S_rev :
        if i == 'b' :
            ans += 'd'
        elif i == 'd' :
            ans += 'b'
        elif i == 'q' :
            ans += 'p' 
        else :
            ans += 'q'
            
    print(f"#{t} {ans}")