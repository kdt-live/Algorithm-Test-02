# 직사각형 길이 찾기
# 3
# 1 1 2
# 4 3 4
# 5 5 5

# T = int(input())
# d = 0
# for test_case in range(1, T + 1):
#     a, b, c= map(int,input().split())
#     if a == b == c :
#         d = a
#     elif a == b != c :
#         d = c
#     elif a == c != b :
#         d = b
#     print(f'# {test_case} {d}')

T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    d = 0
    if a == c:
        d += b
    elif a == b:
        d += c
    elif b == c:
        d += a
    print(f"#{i+1} {d}")
