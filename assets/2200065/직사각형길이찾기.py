# 3456 직사각형 길이 찾기

for i in range(1,int(input())+1):
    a,b,c= map(int,input().split())
    n = [a,b,c]
    if sorted(n)[0] == sorted(n)[1]:
        print(f'#{i} {sorted(n)[2]}')
    else:
        print(f'#{i} {sorted(n)[0]}')
