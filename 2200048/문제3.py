# 3번
T = int(input())
string = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'}
for i in range(1,T+1):
    out = []
    mir = list(input())
    mir = sorted(mir,reverse=True)
    for k in mir:
        out.append(string[k])
    print(f'#{i}',''.join(out))