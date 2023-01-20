'''
신용카드 만들기1
'''
T = int(input())
for _ in range(1,T+1):
    n = list(map(int,input().split()))
    odd = 0
    even = 0
    r = 0
    for i in range(n):
        if i % 2== 1:
            odd = odd*2 + odd
        elif i % 2 ==0:
            even += 1
        
            new_n=(odd+even+r)/10
            print(f'#{i} {new_n}')
