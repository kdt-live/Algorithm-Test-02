a=int(input())
for i in range(a):
    dic={

    }
    test_num=int(input())
    
    score=list(map(int,(input().split())))
    for j in score:
        if j in dic:
            dic[j]+=1
        else:
            dic[j]=1
    
    max_value=0
    max_key=0    
    for k in dic:
        
        
        if dic[k]>max_value:
            max_value=dic[k]
            max_key=k
            
    print('#'+str(test_num),max_key)
