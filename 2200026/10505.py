# import sys
# sys.stdin = open("/Users/daeun/Desktop/멀캠/python/week03/input.txt", "r")


T = int(input())  # 3
for t in range(1, T + 1):
    N = int(input())  # 7 / 10 / 7
    num = list(map(int, input().split()))
    total = sum(num) / len(num)
    cnt = 0
    for i in num:
        if i <= total:
            cnt += 1
    print(f'#{t} {cnt}')


# 첫번째 짠 코드인데 fail나옴.. 왜지?
# 예외 케이스가 있는 것 같은데 예외 케이스가 뭔지 모르겠다
# T = int(input())  # 3
# for t in range(1, T + 1):
#     N = int(input())  # 7 / 10 / 7
#     num = list(map(int, input().split()))
#     # 나머지가 0이라면 길이를 출력하고
#     if sum(num) % len(num) == 0:
#         print(f'#{t} {len(num)}')
#     # 그게 아니라면 나머지를 출력한다.
#     else:
#         div = sum(num) % len(num)
#         print(f'#{t} {div}')
