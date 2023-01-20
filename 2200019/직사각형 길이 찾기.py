from collections import Counter

T = int(input())

for i in range(1,T+1):
    a = list(map(int,input().split()))
    a_dict = Counter(a)
    for key,value in a_dict.items():
        if value == 3:
            wanted = key
        elif value == 1:
            wanted = key
        
    print(f'#{i} {wanted}')