# 문제 5 : 직사각형 길이 찾기
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b:
        d = c
    else:
        if a == c:
            d = b
        else:
            d = a
    print(f'#{t} {d}')