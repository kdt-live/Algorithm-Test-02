for t in range(1, int(input())+1):
    a = input()
    change = {'b':'d',
              'd':'b',
              'q':'p',
              'p':'q'}
    result = ''
    for i in range(len(a)-1,-1,-1):
        result += change[a[i]]    
    print(f'#{t} {result}')