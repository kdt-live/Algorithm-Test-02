T = int(input())
for t in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b == c: # 정사각형일 경우에...
        print(f"#{t} {a}") # a출력
    elif a == b: # a,b가 같으면
        print(f"#{t} {c}") # 나머지 하나 출력
    elif b == c:
        print(f"#{t} {a}")
    elif a == c:
        print(f"#{t} {b}")