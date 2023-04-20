T = int(input())

for i in range(10):
    n = input().split()
    if n[0] == '3':
        n1 = 1
    elif n[0] == '4':
        n1 = 1
    elif n[0] == '5':
        n1 = 1 
    elif n[0] == '6':
        n1 = 1
    elif n[0] == '9':
        n1 = 1
    else:
        n1 = 0
    print(f'#{i+1} {n1}')