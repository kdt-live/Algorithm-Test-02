import collections
from collections import Counter

# 아래 풀이는 vscode에서 잘 되는데 swea 제출에서 계속 fail ...
# 이유가 뭘까?

T = int(input())
for t in range(1, T+1):
    my_dict = dict(collections.Counter(list(map(int, input().split()))))
    many = sorted(my_dict.items(), key=lambda x: x[0])[-1]
    largest = []
    for key in my_dict.keys():
        if my_dict[key] == many[1]:
            largest.append(key)

    print(f'#{t} {max(largest)}')

# 다른 풀이
T = int(input())
for t in range(1, T+1):
    my_dict = dict(collections.Counter(list(map(int, input().split()))))
    largest = []
    for value in my_dict.values():
        for value_ in my_dict.values():
            if value >= value_:
                largest_v = value
    for key in my_dict.keys():
        if my_dict[key] == largest_v:
            largest.append(key)
    print(f'#{t} {max(largest)}')
