# 많이 나온 수

T = int(input())

for t in range(T):
    test_case = int(input())

    scores = list(map(int, input().split()))
    dict = {}

    for i in scores:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    max_num = max(dict, key=dict.get)
    print(max_num)
    
 