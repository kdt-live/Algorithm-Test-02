import sys
sys.stdin = open("예제입력.txt", "r")

T = int(input())
for t in range(1, T+1):
    num = list(map(int,input().split()))

    odd = num[0:17:2]
    even = num[1:16:2]
    even_result = sum(even)
    odd_result = 0
    for i in odd:
        i = i*2
        odd_result += i
        result = 10-((int(even_result)+int(odd_result))%10)
    if (result) == 10:
        print(f'#{t} {0}')
    else:
        print(f'#{t} {result}')