T = int(input())

for t in range(T):
    credit = list(map(int, input().split()))
    sum = 0

    for i in range (len(credit)):
        if ((i+1)%2 == 1):
            sum += credit[i] * 2
        
        else:
            sum += credit[i]
    
    if (sum%10 == 0):
        N = 0
    else:
        N = 10 - (sum % 10)

    print(f'#{t+1} {N}')