# s/w 문제해결 기본 1일차 - 최빈수 구하기

for i in range(1,int(input())+1):
    t = int(input())
    m = list(map(int,input().split()))
    n ={}
    value = []
    key = []
    for a in m:
        if a not in n:
            n[a] = 1
        else :
            n[a] += 1
    for v in n.values():
        value.append(v)
    for k in n:
        if n[k] == max(value):
            key.append(k)
    print(f'#{t}', max(key))
