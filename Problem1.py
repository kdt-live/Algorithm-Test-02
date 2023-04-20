t = int(input())
for i in range(1, t+1) :
    case = int(input())
    s = list(map(int,input().split()))
    dic = {}
    for i in s :
        if i not in dic :
            dic[i] = 1
        else :
            dic[i] +=1
    max_key = max(dic, key=dic.get)
    print(f"#{case} {max_key}")
