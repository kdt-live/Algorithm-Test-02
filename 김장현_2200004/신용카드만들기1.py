t = int(input())

for i in range(1, t+1):
    number_list = list(map(int, input().split()))
    luhn = 0
    for j in range(0, 16, 2):
        luhn += (number_list[j]*2)
    for k in range(1, 15, 2):
        luhn += number_list[k]
    print(f'#{i}', (10-(luhn%10))%10)