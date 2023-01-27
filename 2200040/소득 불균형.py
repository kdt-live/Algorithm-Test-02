# T 테스트수 첫번째 테스트 수

T = int(input())

for t in range(1, T+1):
    cnt = 0
    a = int(input())
    n = list(map(int, input().split()))
    b = sum(n)/len(n)
    for i in n:
        if i<=b:
            cnt += 1
    print(f"#{t} {cnt}")