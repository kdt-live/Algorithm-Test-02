a = int(input())

for i in range(a):
    m = 0
    l = list(map(int,input().split()))
    for j in range(len(l)):
        if j%2 == 0 :
            m+=2*l[j]
        else :
            m+=l[j]

    print (f'#{i+1} {(10-m%10)%10}')