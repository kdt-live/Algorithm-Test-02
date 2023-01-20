# 최빈수 구하기

T = int(input())

for i in range(1, T+1):
    test_num = input()
    scores = list(map(int, input().split()))
    frequency = [0] * 101
    result = 0
    for score in scores:
        frequency[score] += 1
        if frequency[score] >= frequency[result]:
            result = score
    print(f'#{i} {result}')