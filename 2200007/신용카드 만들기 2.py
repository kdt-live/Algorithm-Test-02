T = int(input())
 
for t in range (1, T+1) :
    N = input()
    S = ''
    S = N.replace('-', '')
 
    if S[0] == '3' or S[0] == '4' or S[0] == '5' or S[0] == '6' or S[0] == '9' :
        if len(S) == 16 :
            print(f"#{t} 1")
        else :
            print(f"#{t} 0")
    else :
        print(f"#{t} 0")