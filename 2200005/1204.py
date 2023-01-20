a= int(input())
for i in range(a):
    num = input()
    d = {}
    l = list(map(int,input().split()))
    for j in l:
        d[j] = d.get(j,0) +1
    l2 = sorted(d.items(),key=lambda x:-x[1])
    l3= []
    for k in l2:
        l3.append(l2[0][0])
        if k[1] == l2[0][1]:
            l3.append(k[0])
        else:
            break
        print(f'#{i+1} {max(l3)}')