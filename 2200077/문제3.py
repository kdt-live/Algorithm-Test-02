# 문자열 거울 

T = int(input())

for t in range(T):
    S = input()
    n_S = S[::-1]
    result = ""

    for i in n_S:
        if i == 'p':
            result += 'q'
        elif i == 'q':
            result += 'p'
        elif i == 'b':
            result += 'd'
        elif i == 'd':
            result += 'b'
            
    print(f'#{t+1} {result}')
