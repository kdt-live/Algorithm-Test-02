# 6. 
T = int(input())

for t in range(1,T + 1) :
    nothing = input()
    dict_count100 = {}
    numbers = map(int,input().split())

    for number in numbers :
        dict_count100[number] = dict_count100.get(number,0) + 1

    print(f'#{t} {sorted(dict_count100.items(), key=lambda x : x[1], reverse = True)[0][0]}')
