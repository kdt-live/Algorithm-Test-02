i_t = int(input())
dict_mirror = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}
for i_1 in range(i_t):
    s_input = input()[::-1]
    s_new = ''
    for i_2 in range(len(s_input)):
        s_new += dict_mirror[s_input[i_2]]
    print(f'#{i_1 + 1} {s_new}')