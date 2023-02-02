# 1. 
T = int(input())

for t in range(1,T + 1) :
    tnf = 1
    numbers = input().replace('-','')
    if (int(numbers[0]) not in [3, 4, 5, 6, 9]) or len(numbers) !=16 :
        tnf = 0
    print(f'#{t} {tnf}')

