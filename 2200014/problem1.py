a=int(input())

for i in range(a):
    b=input()
    
    c=[]
    
    for j in b:
        
        c.append(j)
        
    if c[0]!='3' and c[0]!='4' and c[0]!='5' and c[0]!='6' and c[0]!='9':
        
        print('#'+str(i+1), 0)
        
    else:
        for k in c:
            if k=='-':
                c.remove(k)
        if len(c)==16:
            print('#'+str(i+1), 1)
        else:
            print('#'+str(i+1), 0)

