t = int(input())
mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

for i in range(1, t+1):
    text = list(input())
    answer = []
    for j in range(len(text)):
        try:
            answer.insert(0, mirror[text[j]])
        except:
            answer.append(mirror[text[j]])
    print(f'#{i}', end=' ')
    print(*answer, sep='')




