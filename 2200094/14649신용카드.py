T = int(input())

for t in range(1, T+1):
    number = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in range(0, 16, 2):
        odd += number[i] * 2
    for x in range(1, 15, 2):
        even += number[x]
        result = odd + even
        if result % 10 == 0:
            print(0)
        # 마지막 숫자를 구하는 방법을 모르겠다
