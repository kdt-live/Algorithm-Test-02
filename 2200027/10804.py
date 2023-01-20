t = int(input())
mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

for i in range(1, t+1):
    text = list(input())
    answer = []
    for j in range(len(text)):
        try:
            answer.insert(0, mirror[text[j]]) #거울처럼 거꾸로 추가
        except:
            answer.append(mirror[text[j]])
    print(f'#{i} ' + ''.join(answer))