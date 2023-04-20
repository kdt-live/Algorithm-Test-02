T = int(input())



for t in range(1, T+1):
    word = input()
    worddic = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'}
    result = ' '
    for i in word:
        result += worddic[i]
    print(f'#{t} {result[::-1]}')
