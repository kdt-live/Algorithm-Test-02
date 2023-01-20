a = int(input())
for i in range(a):
    string  = input()
    mir=''
    for l in string:
        if l == 'b':
            mir = 'd' +mir
        elif l =='d':
            mir = 'b' +mir
        elif l == 'p':
            mir = 'q' +mir
        else :
            mir = 'p' +mir
        
    print(f'#{i+1} {mir}')