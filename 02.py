# 문자열의 거울 상

T = int(input())

for t in range(1,T+1):
    word = input() # 문자로 입력 받기 
    a = '' 
    for i in word[::-1]: # 거꾸로 range
        if i == 'b':
            a  += 'd'
            
        elif i == 'd':
            a += 'b'
        
        elif i == 'p':
            a += 'q'

        elif i == 'q':
            a += 'p'

    print(f'#{t} {a}')