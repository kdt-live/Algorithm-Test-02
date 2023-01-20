# 최빈수 구하기

T = int(input())
for i in range(1, T+1):
    t = int(input())
    dict1 = {}
    score = list(map(int, input().split()))
    for j in score:
        if j not in dict1:
            dict1[j] = 1
        else:
            dict1[j] += 1
    a = sorted(dict1.items(), key = lambda x :x[1], reverse=True)
    print(a[0][0])
   
    
