# 직사각형의 길이 찾기

T = int(input())
for i in range(1, T + 1):
    a, b, c = list(map(int,input().split()))
    x = set([a, b, c])
    y = list(x)
    if a == b == c:
        print(f"#{i} {a}")
    else:
        common = a + b + c - y[0] - y[1]
        result = y[0] + y[1] - common
        print(f"#{i} {result}")