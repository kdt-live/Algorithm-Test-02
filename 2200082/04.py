mirrored_char = {
    'b':'d',
    'd':'b',
    'p':'q',
    'q':'p'
}

T = int(input())
for t in range(1, T+1):
    t_str = input()
    r_t_str = t_str[::-1]
    in_mirror = ''
    for char in r_t_str:
        in_mirror += mirrored_char[char]
    
    print(f'#{t} {in_mirror}')





    in_mirror

