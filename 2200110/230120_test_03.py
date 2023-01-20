T = int(input())
for t in range(1, T+1):
    mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

    my_str = input()
    new_str = ''
    for i in my_str:
        new_str += mirror[i]

    print(f'#{t} {new_str[::-1]}')
