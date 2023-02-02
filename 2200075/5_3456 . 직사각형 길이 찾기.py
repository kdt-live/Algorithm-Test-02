# 4. 
T = int(input())

for t in range(1,T + 1) :
    numbers = list(map(int,input().split()))
    numbers_set = set(numbers)
    for number in numbers_set :
        if numbers.count(number) % 2 == 1 :
            print(f'#{t} {number}')
