t = int(input())
for i in range(1, t+1) :
    n = list(map(int, input().split()))
    dict = {}
    for j in n :
        if j not in dict :
            dict[j] = 1
        else :
            dict[j] +=1
    for key, values in dict.items() :
        if values == 1:
            print(f"#{i} {key}")
        elif values == 3:
            print(f"#{i} {key}")