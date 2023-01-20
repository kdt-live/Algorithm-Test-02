T = int(input())

for test_case in range(1, T + 1):
    card = list(map(int, input().split()))

    odds = [card[number]*2 for number in range(0, len(card), 2)]
    evens = [card[number] for number in range(1, len(card), 2)]

    result = 10 - ((sum(odds) + sum(evens)) % 10) if (sum(odds) + sum(evens)) % 10 != 0 else 0

    print(f'#{test_case} {result}')