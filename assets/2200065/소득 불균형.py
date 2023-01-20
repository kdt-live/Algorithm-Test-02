# 10505 소득불균형

for i in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int,input().split()))
    m = []
    for x in lst:
        if x <= (sum(lst)/n):
            m.append(x)
    print(f'#{i} {len(m)}')