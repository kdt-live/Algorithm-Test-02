T = int(input())

for test_case in range(1, T + 1):
    people = int(input())
    money = list(map(int, input().split()))

    average = sum(money) / people
    result = [1 for m in money if m <= average]

    print(f'#{test_case} {sum(result)}')