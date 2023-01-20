a=int(input())
for i in range(a):
    dic={

    }
    l1=list(map(int,input().split()))
    for j in l1:
        
        if j in dic:
            dic[j]+=1
        else:
            dic[j]=1
    

    for k in dic:
        if dic[k]%2==1:
            print('#'+str(i+1),k)
