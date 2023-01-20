T = int(input())

reverse_dict = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',
}

for test_case in range(1, T + 1):
    string = input()
    new_string = ''

    for char in string[::-1]:
        new_string += reverse_dict[char]

    print(f'#{test_case} {new_string}')