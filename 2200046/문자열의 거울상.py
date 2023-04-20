mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

t = int(input())

for i in range(t):
    string = input()
    print(f'#{i + 1} ', end = '')

    for j in range(len(string) - 1, -1, -1):
        print(mirror[string[j]], end = '')

    print()