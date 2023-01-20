T = int(input())
mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
for t in range(1, T+1):
    string = input()
    print(f'#{t} ', end='')
    for s in string[::-1]:
        print(f'{mirror.get(s)}', end='')
    print()