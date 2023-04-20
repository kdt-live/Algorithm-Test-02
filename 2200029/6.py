import sys
sys.stdin = open("예제입력 (1).txt", "r")
    
T = int(input())
for t in range(1, T + 1):
    strings = input()
    essential = ["3", "4", "5", "6", "9"]  
    cnt = strings.count("-")
    if strings[0] in essential and len(strings) - cnt == 16:  
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')

# strings[0]은 문자열이다. 따라서 essential에서 숫자를 문자형으로 해야된다.