# 2.
T = int(input())

for t in range(1,T + 1) :
    numbers = list(map(int, input().split()))
    sum_number = 0

    for i in range(0, len(numbers), 2) : # 홀수
        sum_number += numbers[i]
    sum_number *= 2

    for i in range(1, len(numbers), 2) : # 짝수
        sum_number += numbers[i]
    if (sum_number % 10 == 0) :
        print(f'#{t} {sum_number % 10}')
    else :
        print(f'#{t} {round(sum_number + 5, -1) - sum_number}')