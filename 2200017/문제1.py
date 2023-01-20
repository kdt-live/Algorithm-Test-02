# 1204
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    l = [0 for i in range(101)]
    m = 0
    for s in score: # 최빈수 찾기
        l[s] += 1
        if l[s] >= l[m]:
            m = s

    print(f'#{t} {m}')