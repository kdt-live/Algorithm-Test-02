T = int(input())
for _ in range(T):
    case = int(input())
    dic = {}
    lst = [int(x) for x in input().split()]
    for i in lst:
        dic[i] = dic.get(i, 0) + 1
    max_num = sorted(dic, key=lambda x: dic[x], reverse=True)[0]
    print(f'#{case} {max_num}')