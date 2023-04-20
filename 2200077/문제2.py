# 신용카드 번호1

T = int(input())

for t in range(T):
    result = 0

    n = list(map(int, input().split()))

    for i in range(15):
        if i % 2 == 0: # 여기서는 홀수임
            result += (n[i] * 2)
        else:
            result += n[i]

    for j in range(10):
        if (j + result) % 10 == 0:
            print(f'#{t+1} {j}') 