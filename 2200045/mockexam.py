# 1. 신용카드 만들기 2

T = int(input())

for t in range(1, T+1):
    card = input()
    if len(card) < 16:
        print(f'#{t} 0')
    elif len(card) > 16:
        card = card[:4] + card[5:9] + card[10:14] + card[15:]
        if card[0] == '3' or card[0] == '4' or card[0] == '5' or card[0] == '6' or card[0] == '9':
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    else:
        if card[0] == '3' or card[0] == '4' or card[0] == '5' or card[0] == '6' or card[0] == '9':
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')

    


# 2. 신용카드 만들기 1

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    N = 0

    for n in range(1, len(numbers) + 1):
        if n % 2 == 1:
            N += numbers[n -1] * 2
        else:
            N += numbers[n -1]

    if 10 - (N % 10) == 10:
        thenumber = 0
    else:
        thenumber = 10 - (N % 10)

    print(f'#{t} {thenumber}')
    





# 3. 문자열의 거울상 

T = int(input())
mirror = {'b':'d','d':'b','p':'q','q':'p'}

for t in range(1, T+1):
    string = input()
    result = ''
    for n in string[::-1]:
        result += mirror[n]
    print(f'#{t} {result}')

# 4. 소득 불균형 

T = int(input())

for t in range(1, T+1):
    people = int(input())
    income = list(map(int, input().split()))
    under = 0
    for a in income:
        avg = sum(income) // people
        if a <= avg:
            under += 1
    print(f'#{t} {under}')




# 5. 직사각형 길이 찾기 

T = int(input())

for t in range(1, T+1):
    (a, b, c) = list(map(int, input().split()))
    if a == b:
        print(f'#{t} {c}')
    elif a == c:
        print(f'#{t} {b}')
    else:
        print(f'#{t} {a}')



# 6. 1일차 - 최빈수 구하기 

T = int(input())

for t in range(1, T+1):
    order = int(input())
    count = {0:0}
    biggest = 0

    numbers = list(map(int, input().split()))
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    
    for a in count:

        if count[a] > count[biggest]:
            biggest = a
        elif count[a] == count[biggest]:
            if a > biggest:
                biggest = a
    
    print(f'#{order} {biggest}')