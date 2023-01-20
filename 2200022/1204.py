# 1204 [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2

T = int(input())
for i in range(T):
    C = int(input())
    numbers = list(map(int, input().split()))
    for i in numbers:
        dic = dict.fromkeys(numbers, numbers.count(i))
        print(dic)
        # print(f"#{T} {key}")