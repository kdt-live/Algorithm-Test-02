T = int(input())

for tc in range(1,T+1):
    N = int(input())
    
    income = list(map(int,input().split()))

    avg = sum(income) / N
    ans = 0
    for i in income:
        if avg >= i:
            ans += 1
    print("#{} {}".format(tc,ans))
