# 1204번 - 최빈수 구하기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    score_list = [0] * 101
    max_mode = 0
    for i in score:
        score_list[i] += 1
        if score_list[i] >= score_list[max_mode]:
            max_mode = i
    print(f'#{tc} {max_mode}')