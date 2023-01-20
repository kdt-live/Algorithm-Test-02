a= int(input())
for i in range(a):
    a,b,c= map(int,input().split())
    print(f'#{i+1} {a^b^c}')