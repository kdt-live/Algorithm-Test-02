#문자열의 거울상
T = int(input())
for i in range(1,T+1):
    rev_s = ''
    s = input()
    for j in range(len(s)):
        if s[-j-1] == 'b': 
            rev_s += 'd'
        elif s[-j-1] == 'd': 
            rev_s += 'b'
        elif s[-j-1] == 'p': 
            rev_s += 'q'
        elif s[-j-1] == 'q': 
            rev_s += 'p'
    print(f'#{i} {rev_s}')
