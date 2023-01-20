T = int(input())
a = {}
for _ in range(T):
    number = int(input())
    score = list(map(int,input().split()))
    for i in score :
        if i in a :
            a[i] += 1
        else:
            a[i] = 1
    b = list(sorted(a.items(), key=lambda x:x[1],reverse=True))
    b = str(b)
    print(f'#{_} {b[2:4]}')