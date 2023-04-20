# 직사각형 길이 찾기 

T = int(input())
num = []

for t in range(1,T+1):
    a, b, c = list(map(int,input().split())) 
   
    if a != b:
        d = a + b - c
        print(f'#{t} {d}')
    elif a == b == c:
        e = a
        print(f'#{t} {e}')
    elif b != c:
        f = a + c - b
        print(f'#{t} {f}')
