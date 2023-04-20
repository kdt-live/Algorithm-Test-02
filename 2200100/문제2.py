T = int(input())
for t in range(T):
    a , b, c = map(int,input().split())
    A = [a,b,c]
    d = (max(A)+min(A))*2 - a - b - c
    print(f'#{t+1} {d}')