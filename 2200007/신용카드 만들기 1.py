T = int(input())

for t in range (1, T+1) :
    N = list(map(int,input().split()))
    sum = 0
    ans = 0
    for n in range (0, len(N)) :
        if n%2 == 0 :
            sum += N[n]*2
        else :
            sum += N[n]
    for i in range (0, 10) :
        if (sum + i)%10 == 0 :
            ans = i
    print(f"#{t} {ans}")