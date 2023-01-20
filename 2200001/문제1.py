# 최빈수 구하기
T = int(input())

for t in range(1, T+1):
    score = list(map(int, input().split()))
    max_score = 0

    for i in range(101):
        if score.count(i) >= score.count(max_score):
            max_score = i

    print(f'#{t} {max_score}')        