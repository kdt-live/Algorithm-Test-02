# 6. 
T = int(input())

for t in range(1,T + 1) :
    nothing = input()
    dict_count100 = {}
    numbers = map(int,input().split())

    for number in numbers :
        dict_count100[number] = dict_count100.get(number,0) + 1

    for number in dict_count100 :
        if max(dict_count100.values()) == dict_count100[number] :
            print(f'#{t} {number}')
            break

