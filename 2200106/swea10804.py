t = int(input())
my_dict = {
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p'
}
for tc in range(1, t+1):
    words = input()
    words = words[::-1]
    #print(words)
    mirror = ''

    for ele in words:
        mirror += my_dict[ele]
    
    print(f'#{tc} {mirror}')