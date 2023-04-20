import sys
sys.stdin = open("input (5).txt", "r")

T = int(input())
for t in range(1, T + 1):
    string = input()
    mirror = {"b": "d", "d": "b", "p": "q", "q": "p"}
    new_list = []
    for alpha in string:
        new_list.append(mirror[alpha])
        result_list = new_list[::-1]
    result = ""
    for i in result_list:
        result += i
    print(f'#{t} {result}')
        
        
        