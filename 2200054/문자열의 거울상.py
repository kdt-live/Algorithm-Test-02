import sys
input = sys.stdin.readline

TC = int(input())
for t in range(1, TC+1):
    string = input().rstrip()
    list = []
    for i in range(len(string)):
        if string[i] == 'b':
            list.append('d')
        elif string[i] == 'd':
            list.append('b')
        elif string[i] == 'p':
            list.append('q')
        elif string[i] == 'q':
            list.append('p')
    list = list[::-1]
    result = ""
    for i in range(len(list)):
        result += list[i]
    
    print(f'#{t} {result}')