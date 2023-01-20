a=int(input())
for i in range(a):
    T=int(input())
    income=list(map(int,input().split()))
    cnt=0
    for j in income:
        if j<=(sum(income)/len(income)):
            cnt+=1
    print('#'+str(i+1),cnt)