a = int(input())
while a:
    for i in range(1,a+1):
        c = 0
        b = list(map(int, input().split())) 
        for j in b:
            d=[]
            d.append(j)
            if d[c] < d[j] : c=j
            print(f"#{i} {c}")
